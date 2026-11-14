# Paper 20 — The Cosmic Time-Landscape ($M_\tau^\star$): Live ESA Euclid DR1-Foundation Validation and Multi-Telescope Atlas of the Zero-Parameter Tau Core Universe Model

**Repository:** `tau-core-euclid-cosmic-time-landscape-paper20`  
**Series:** Tau Core Empirical / Protocol & Cosmological Synthesis Series (Paper 20)  
**Knowledge Base Connection:** `.tau-core-kb -> /Volumes/EXTERNAL/Research/Tau Core/tau-core-ai-knowledge-base`

---

## Main claim

This paper and reproducibility package construct the first data-driven **3D/4D Cosmic Time-Landscape Atlas ($M_\tau^\star = \mathrm{d}\tau/\mathrm{d}t(\mathbf{x}, z)$)** directly from **`18,983` live observational records** retrieved from the newly released **ESA Euclid DR1-Foundation (`2026`) Science Archive** (`eas.esac.esa.int/tap-server/tap/sync`, schema `dr1.*`: `11,383` VIS mosaic footprint tiles and `5,955` unique 3D-mapped galaxies and quasars across $0.05 \le z \le 5.49$), combined with multi-telescope benchmark catalogs (`Planck PR3`, `Euclid ERO Abell 2390`, `CLASH-20`, `X-COP-12`, `LoCuSS-41`, `CCCP-26`, `SPT-WTG-19`, `HSC-XXL-43`, `JWST+HST`, `JWST+ALMA`, `SLACS-70`, `TDCOSMO-7`, `SPARC-171`, `Gaia DR3`, and `NANOGrav 15-yr`).

Under the source-frozen, zero-free-parameter ($k = 0$) **Tau Core (`v19`)** terminal invariants:
- $\alpha_{\mathrm{OCSR}} = \frac{20\sqrt{3}}{51} \approx 0.67923561$, $a_0(0) = 1.18076 \times 10^{-10}\;\mathrm{m/s^2}$,
- $\frac{\Omega_{A,\mathrm{eff}}}{\Omega_b} = \frac{213\sqrt{3} - 20}{65} \approx 5.36810495$ ($0.06\sigma$ parity with `Planck PR3` $\Omega_{\mathrm{DM}}/\Omega_b = 5.364 \pm 0.065$),
- $a_0^{\mathrm{KH}}(z) = a_0(0)\,E(z)\,\frac{|1 - \frac{3}{4}\Omega_m(z)|}{|1 - \frac{3}{4}\Omega_{m,0}|}$ with exact inflection minimum at $z_{\mathrm{dip}} = \left(2\frac{1 - \Omega_{m,0}}{\Omega_{m,0}}\right)^{1/3} - 1 = 0.6316$,

the package demonstrates that:
1. **Clock Valleys ($\mathrm{d}\tau/\mathrm{d}t < 1$, apparent "dark matter"):** In live Euclid DR1 galaxies (median $R_{\mathrm{eff}} = 3.825\;\mathrm{kpc}$, median $g_{\mathrm{bar}}(R_{\mathrm{eff}}) = 6.704 \times 10^{-11}\;\mathrm{m/s^2} = 0.568\,a_0(0)$), temporal refraction produces a median $1.544\times$ circular-velocity boost over pure Baryonic GR ($133.65\;\mathrm{km/s}$ vs. $84.75\;\mathrm{km/s}$) and a $15.7\times$ excess surface mass density boost $\Delta\Sigma_{\mathrm{Tau}}(200\;\mathrm{kpc}) = 7.082\;M_\odot/\mathrm{pc}^2$ around `524` real Euclid DR1 massive foreground lenses, while `2,192` overdense filament/cluster galaxies exhibit clock retardation down to $-520.89\;\mathrm{ppm}$.
2. **Clock Hills ($\mathrm{d}\tau/\mathrm{d}t > 1$, apparent "dark energy"):** Across `2,583` underdense void galaxies in the live Euclid DR1 catalog, local cosmic clocks run faster by up to $+79.60\;\mathrm{ppm}$ relative to the mean FLRW background, while in the `Eridanus Supervoid` ($z \approx 0.15$) the $+49.6\;\mathrm{ppm}$ clock speedup yields $\Delta T_{\mathrm{Tau}}(0) = -148.5\;\mu\mathrm{K}$ ($\chi^2_\nu = 0.42$), resolving the `Planck CMB Cold Spot` anomaly.

## Does not claim

Following the central Tau Core AI Knowledge Base claim-boundary discipline (`.tau-core-kb/CLAIM_BOUNDARIES.md`):
- **Upstream parent selection remains open (`NATURE_LEVEL_CLOSURE = false`):** While the terminal astrophysical readout equations operate with $k = 0$ free tuned parameters once the `v19` invariants are imported, unconditional upstream parent-branch selection in the Foundation Series (`Paper I`, `Paper IV`, `Paper VII-A`) remains open.
- **Low-mass group gas-evacuation boundary ($T_X < 2.5\;\mathrm{keV}$):** In low-mass galaxy groups (`HSC-XXL` low-mass subset, $N = 13$), strong AGN feedback evacuates baryonic gas beyond $R_{500}$ ($Y_b^{\mathrm{obs}} \approx 0.433$), so applying the massive-cluster shock-containment boundary ($u_{\mathrm{sh}} = 1.35\,R_{200}$) underpredicts low-mass group masses (median $M_{\mathrm{Tau}}/M_{\mathrm{WL}} = 0.68$).
- **Linear CMB degeneracy:** On the `Planck Plik_lite` `613x613` covariance matrix, Tau Core ($k_{\mathrm{DM}} = 0$) and $\Lambda\mathrm{CDM}$ ($k_{\mathrm{DM}} = 1$) are in statistical parity ($\Delta\chi^2 = +0.009$); decisive falsification between the two paradigms resides at the late-time $z_{\mathrm{dip}} = 0.6316$ inflection point and in supervoid clock acceleration.

## Included data

All compact derived catalogs and validation summaries are stored in `data/derived/`:
- `euclid_dr1_footprint_tiles.csv` (`11,383` live Euclid DR1 VIS mosaic tiles)
- `euclid_dr1_spectroscopic_galaxies_live.csv` (`1,500` live NISP emission-line spectra across `359` unique galaxies)
- `euclid_dr1_wide_and_deep_galaxies_live.csv` (`5,500` live Wide + Deep + EDFN galaxies, including `524` massive foreground lenses)
- `euclid_dr1_quasars_live.csv` (`600` live NISP spectroscopic quasars)
- `euclid_dr1_live_time_landscape_catalog.csv` (`5,955` unique 3D-mapped Euclid DR1 objects with $\Delta(\mathrm{d}\tau/\mathrm{d}t)$ [ppm])
- `euclid_dr1_live_validation_results.json`
- `tau_core_universe_model_catalog_v1.csv` (`249` multi-telescope benchmark structures)
- `tau_core_universe_model_validation_v1.json`
- `paper20_euclid_dr1_field_summary.csv`
- `paper20_multi_telescope_benchmark_summary.csv`

## Reproduce

Run the full deterministic reproduction pipeline from the repository root:

```bash
python3 scripts/reproduce.py
```

This command:
1. Regenerates the compact derived summaries and all 7 high-resolution (`300 DPI`) figures (`scripts/generate_paper20_figures_and_summaries.py`),
2. Compiles `paper20_submission_source/main.tex` to `paper20_submission_source/main.pdf` (and `paper20_hungarian_source/main.tex` to `paper20_hungarian_source/main.pdf`),
3. Builds `arxiv_submission_source.zip` (`scripts/build_arxiv_source.py`),
4. Runs the automated verification test suite (`pytest -q`), and
5. Prints `PAPER20_EUCLID_TIME_LANDSCAPE_REPRODUCTION_COMPLETE`.

## arXiv source package

- English submission source: `paper20_submission_source/` (`main.tex`, `refs.bib`, `figures/`, compiled `main.pdf`)
- Hungarian companion source: `paper20_hungarian_source/` (`main.tex`, `refs.bib`, `figures/`, compiled `main.pdf`)
- Source-only archive: `arxiv_submission_source.zip`

## Scope

Empirical multi-telescope validation and 3D cosmic time-landscape cartography under the source-frozen `v19` ($k = 0$) terminal readout invariants, paired with explicit upstream claim boundaries and pre-registered Euclid DR1 / SKA falsification gates.
