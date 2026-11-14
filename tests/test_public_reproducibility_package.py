"""
Automated reproducibility and epistemic-boundary verification suite for Paper 20:
`tau-core-euclid-cosmic-time-landscape-paper20`.
"""

import json
import math
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

    assert en_tex.exists() and en_tex.stat().st_size > 5000
    assert en_pdf.exists() and en_pdf.stat().st_size > 100_000
    assert hu_tex.exists() and hu_tex.stat().st_size > 5000
    assert hu_pdf.exists() and hu_pdf.stat().st_size > 100_000


def test_all_seven_figures_exist_across_directories():
    for fig_name in EXPECTED_FIGURES:
        for sub in ["figures", "paper20_submission_source/figures", "paper20_hungarian_source/figures"]:
            fig_path = REPO_ROOT / sub / fig_name
            assert fig_path.exists(), f"Missing figure {fig_path}"
            assert fig_path.stat().st_size > 50_000, f"Figure too small: {fig_path}"


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


def test_live_euclid_dr1_validation_json_and_zero_parameter_invariants():
    json_path = REPO_ROOT / "data" / "derived" / "euclid_dr1_live_validation_results.json"
    assert json_path.exists()
    data = json.loads(json_path.read_text(encoding="utf-8"))

    # Verify live Euclid DR1 record counts
    assert data["total_live_records_downloaded"] == 18983
    counts = data["datasets"]
    assert counts["vis_mosaic_footprint_tiles"] == 11383
    assert counts["nisp_spectroscopic_galaxy_lines"] == 1500
    assert counts["nisp_unique_spectroscopic_galaxies"] == 359
    assert counts["mer_phz_wide_deep_edfn_galaxies"] == 5500
    assert counts["nisp_spectroscopic_quasars"] == 600
    assert counts["combined_unique_extragalactic_objects"] == 5955

    # Verify exact k=0 Tau Core invariants
    invariants = data["tau_core_v19_zero_parameter_constants"]
    assert invariants["k_free_parameters"] == 0
    assert math.isclose(invariants["alpha_OCSR"], 20.0 * math.sqrt(3.0) / 51.0, rel_tol=1e-6)
    assert math.isclose(invariants["Omega_m_over_Omega_b"], 1.0 + (213.0 * math.sqrt(3.0) - 20.0) / 65.0, rel_tol=1e-6)
    assert math.isclose(invariants["z_dip_inflection"], 0.6316, abs_tol=2e-3)

    # Verify 524 strong/weak lensing foreground candidates
    val2 = data["validation_2_massive_foreground_lens_weak_lensing"]
    assert val2["n_massive_foreground_lenses"] == 524
    assert val2["DeltaSigma_Tau_at_200kpc_Msun_pc2"] > 7.0
    assert val2["DeltaSigma_bar_at_200kpc_Msun_pc2"] < 0.60
    assert val2["lensing_boost_over_GR_at_200kpc"] > 15.0


def test_claim_boundary_and_ownership_ledger_markers():
    readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    en_tex_text = (REPO_ROOT / "paper20_submission_source" / "main.tex").read_text(encoding="utf-8")
    hu_tex_text = (REPO_ROOT / "paper20_hungarian_source" / "main.tex").read_text(encoding="utf-8")

    for text in (readme_text, en_tex_text, hu_tex_text):
        assert "NATURE" in text and "CLOSURE" in text
        assert "2.5" in text and "keV" in text
        assert "18" in text and "983" in text
