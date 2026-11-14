"""
Automated reproducibility, canonical k=0 invariant, LaTeX log hygiene, and
epistemic-boundary verification suite for Paper 20:
`tau-core-euclid-cosmic-time-landscape-paper20`.
"""

import csv
import json
import math
import re
from pathlib import Path
import zipfile

REPO_ROOT = Path(__file__).resolve().parent.parent

EXPECTED_FIGURES = [
    "fig1_tau_cosmic_time_landscape_mechanism_and_blackhole_duality.png",
    "fig2_live_euclid_dr1_master_atlas.png",
    "fig3_allsky_mollweide_clock_atlas.png",
    "fig4_conformal_spacetime_wedge.png",
    "fig5_multi_telescope_validation_panel.png",
    "fig6_euclid_deep_fields_eridanus_tomography.png",
    "fig7_wiltshire_timescape_vs_tau_core_and_falsification_matrix.png",
]


def test_manuscript_pdfs_and_sources_exist():
    en_tex = REPO_ROOT / "paper20_submission_source" / "main.tex"
    en_pdf = REPO_ROOT / "paper20_submission_source" / "main.pdf"
    hu_tex = REPO_ROOT / "paper20_hungarian_source" / "main.tex"
    hu_pdf = REPO_ROOT / "paper20_hungarian_source" / "main.pdf"

    assert en_tex.exists() and en_tex.stat().st_size > 15_000
    assert en_pdf.exists() and en_pdf.stat().st_size > 100_000
    assert hu_tex.exists() and hu_tex.stat().st_size > 15_000
    assert hu_pdf.exists() and hu_pdf.stat().st_size > 100_000


def test_all_seven_figures_exist_and_are_localized():
    for fig_name in EXPECTED_FIGURES:
        en_root_fig = REPO_ROOT / "figures" / fig_name
        en_sub_fig = REPO_ROOT / "paper20_submission_source" / "figures" / fig_name
        hu_sub_fig = REPO_ROOT / "paper20_hungarian_source" / "figures" / fig_name

        for fig_path in (en_root_fig, en_sub_fig, hu_sub_fig):
            assert fig_path.exists(), f"Missing figure {fig_path}"
            assert fig_path.stat().st_size > 50_000, f"Figure too small: {fig_path}"

        # English root and submission figures must be byte-identical, while Hungarian figure is localized
        assert en_root_fig.read_bytes() == en_sub_fig.read_bytes()
        assert en_sub_fig.read_bytes() != hu_sub_fig.read_bytes(), f"Hungarian figure not localized: {fig_name}"


def test_arxiv_submission_zip_is_clean_and_complete():
    zip_path = REPO_ROOT / "arxiv_submission_source.zip"
    assert zip_path.exists() and zip_path.stat().st_size > 100_000

    with zipfile.ZipFile(zip_path, "r") as zf:
        names = set(zf.namelist())
        assert "main.tex" in names
        assert "refs.bib" in names
        assert "main.bbl" in names
        for fig_name in EXPECTED_FIGURES:
            assert f"figures/{fig_name}" in names
        for name in names:
            assert not name.endswith(".pdf"), f"Compiled PDF leaked into arXiv zip: {name}"
            assert not name.endswith(".aux"), f"Auxiliary file leaked into arXiv zip: {name}"
            assert not name.endswith(".log"), f"Log file leaked into arXiv zip: {name}"


def test_canonical_v19_zero_parameter_invariants_and_json_csv_sync():
    json_path = REPO_ROOT / "data" / "derived" / "euclid_dr1_live_validation_results.json"
    val_json_path = REPO_ROOT / "data" / "derived" / "tau_core_universe_model_validation_v1.json"
    field_csv_path = REPO_ROOT / "data" / "derived" / "paper20_euclid_dr1_field_summary.csv"
    bench_csv_path = REPO_ROOT / "data" / "derived" / "paper20_multi_telescope_benchmark_summary.csv"

    assert json_path.exists() and val_json_path.exists()
    data = json.loads(json_path.read_text(encoding="utf-8"))
    val_data = json.loads(val_json_path.read_text(encoding="utf-8"))

    # Verify live Euclid DR1 record counts
    assert data["total_live_records_downloaded"] == 18983
    counts = data["datasets"]
    assert counts["vis_mosaic_footprint_tiles"] == 11383
    assert counts["nisp_spectroscopic_galaxy_lines"] == 1500
    assert counts["nisp_unique_spectroscopic_galaxies"] == 359
    assert counts["mer_phz_wide_deep_edfn_galaxies"] == 5500
    assert counts["unique_galaxies_with_mer_phz_morphology"] == 5601
    assert counts["nisp_spectroscopic_quasar_lines"] == 600
    assert counts["nisp_spectroscopic_quasars"] == 354
    assert counts["combined_unique_extragalactic_objects"] == 5955

    # Verify canonical k=0 Tau Core v19 invariants (alpha_OCSR = 5*sqrt(3)/24)
    alpha_expected = 5.0 * math.sqrt(3.0) / 24.0
    omega_a_expected = (213.0 * math.sqrt(3.0) - 20.0) / 65.0
    omega_m0 = 0.3153
    z_dip_expected = (2.0 * (1.0 - omega_m0) / omega_m0) ** (1.0 / 3.0) - 1.0

    for inv in (data["tau_core_v19_zero_parameter_constants"], val_data["exact_invariants"]):
        assert math.isclose(inv["alpha_OCSR"], alpha_expected, rel_tol=1e-6)
        assert inv["alpha_OCSR_formula"] == "5*sqrt(3)/24"
        assert math.isclose(inv["c_proj"], 0.5, rel_tol=1e-9)
        assert math.isclose(inv["c_mix"], 1.0 / (4.0 + math.sqrt(3.0)), rel_tol=1e-6)
        assert math.isclose(inv["Omega_A_over_Omega_b"], omega_a_expected, rel_tol=1e-6)
        assert math.isclose(inv["Omega_m_over_Omega_b"], 1.0 + omega_a_expected, rel_tol=1e-6)
        assert math.isclose(inv["a0_Kin_z0_m_s2"], 1.18076e-10, rel_tol=1e-4)
        assert math.isclose(inv["a0_KH_z0_m_s2"], 9.015398e-11, rel_tol=1e-4)

    assert math.isclose(data["tau_core_v19_zero_parameter_constants"]["z_dip_inflection"], z_dip_expected, abs_tol=1e-5)
    assert math.isclose(val_data["exact_invariants"]["z_dip_kodama_hayward_inflection"], z_dip_expected, abs_tol=1e-6)

    # Verify Validation I & II purified k=0 metrics
    val1 = data["validation_1_nisp_spectroscopic_kinematics"]
    assert math.isclose(val1["median_v_Tau_kms"], 114.09, abs_tol=0.05)
    assert math.isclose(val1["median_velocity_boost_factor"], 1.3247, abs_tol=1e-3)

    val2 = data["validation_2_massive_foreground_lens_weak_lensing"]
    assert val2["n_massive_foreground_lenses"] == 524
    assert math.isclose(val2["DeltaSigma_bar_at_200kpc_Msun_pc2"], 0.4292, abs_tol=1e-3)
    assert math.isclose(val2["DeltaSigma_Tau_at_200kpc_Msun_pc2"], 4.0167, abs_tol=1e-3)
    assert math.isclose(val2["DeltaSigma_Tau_TwoSector_at_200kpc_Msun_pc2"], 18.0763, abs_tol=1e-2)
    assert math.isclose(val2["lensing_boost_over_GR_at_200kpc"], 9.36, abs_tol=0.05)
    assert math.isclose(val2["two_sector_lensing_boost_over_GR_at_200kpc"], 42.11, abs_tol=0.1)

    # Verify CSV summaries match JSON
    with open(field_csv_path, "r", encoding="utf-8") as f:
        field_rows = list(csv.DictReader(f))
    assert len(field_rows) == 4
    assert sum(int(r["n_objects"]) for r in field_rows) == 5955
    assert sum(int(r["n_void_faster_clock_gt5ppm"]) for r in field_rows) == 1348
    assert sum(int(r["n_cluster_slower_clock_lt_minus5ppm"]) for r in field_rows) == 665

    with open(bench_csv_path, "r", encoding="utf-8") as f:
        bench_rows = {r["benchmark_id"]: r for r in csv.DictReader(f)}
    assert len(bench_rows) == 12
    assert math.isclose(float(bench_rows["B01_Euclid_DR1_Live_RAR"]["tau_core_k0"]), val1["median_velocity_boost_factor"], abs_tol=1e-4)
    assert math.isclose(float(bench_rows["B02_Euclid_DR1_Live_Lenses"]["tau_core_k0"]), val2["DeltaSigma_Tau_at_200kpc_Msun_pc2"], abs_tol=1e-4)


def test_zero_corrupted_constants_anywhere_in_repo():
    corrupted_pat = re.compile(r"(20\s*\*?\s*(?:math\.|np\.)?sqrt\(3|20\\sqrt\{3\}\s*/\s*51|0\.67923)")
    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or ".pytest_cache" in path.parts:
            continue
        if path.suffix in {".py", ".tex", ".md", ".json", ".csv"}:
            if path.resolve() == Path(__file__).resolve():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            match = corrupted_pat.search(text)
            assert match is None, f"Corrupted 20*sqrt(3)/51 constant found in {path}: {match.group(0)}"


def test_manuscript_text_synchronization_and_claim_boundaries():
    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    en_tex_text = (REPO_ROOT / "paper20_submission_source" / "main.tex").read_text(encoding="utf-8")
    hu_tex_text = (REPO_ROOT / "paper20_hungarian_source" / "main.tex").read_text(encoding="utf-8")

    for text in (readme_text, en_tex_text, hu_tex_text):
        assert "NATURE" in text and "CLOSURE" in text
        assert "EAS-SNPR-N1" in text
        assert "U1/F1" in text
        assert "2.5" in text and "keV" in text
        assert "18" in text and "983" in text
        assert "114.09" in text
        assert "1.3247" in text
        assert "4.01" in text and "18.076" in text
        assert "-153.79" in text
        assert "0.9015" in text


def test_latex_logs_have_zero_overfull_hbox_and_zero_hyperref_warnings():
    overfull_pat = re.compile(r"Overfull \\hbox \(([0-9.]+)pt too wide\)")
    for sub in ("paper20_submission_source", "paper20_hungarian_source"):
        log_path = REPO_ROOT / sub / "main.log"
        assert log_path.exists(), f"Missing LaTeX log: {log_path}"
        log_text = log_path.read_text(encoding="utf-8", errors="ignore")

        for m in overfull_pat.finditer(log_text):
            pts = float(m.group(1))
            assert pts <= 2.0, f"Overfull \\hbox of {pts}pt (> 2.0pt) in {log_path}"

        assert "Package hyperref Warning:" not in log_text, f"hyperref warning in {log_path}"
        assert "pdfTeX warning (ext4):" not in log_text, f"Duplicate PDF anchor in {log_path}"
        assert "LaTeX Warning: Reference" not in log_text, f"Undefined reference in {log_path}"
        assert "LaTeX Warning: Citation" not in log_text, f"Undefined citation in {log_path}"
