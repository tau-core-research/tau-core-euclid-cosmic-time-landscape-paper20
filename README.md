# Paper 20 — The Cosmic Time-Landscape ($M_\tau^\star$): Live ESA Euclid DR1-Foundation Validation and Multi-Telescope Atlas of the Zero-Parameter Tau Core Universe Model

**Repository:** `tau-core-euclid-cosmic-time-landscape-paper20`  
**Series:** Tau Core Empirical / Protocol & Cosmological Synthesis Series (Paper 20)  
**Knowledge Base Connection:** `.tau-core-kb -> /Volumes/EXTERNAL/Research/Tau Core/tau-core-ai-knowledge-base`

---

## Main claim

This paper and reproducibility package construct the first data-driven **3D/4D Cosmic Time-Landscape Atlas ($M_\tau^\star = \mathrm{d}\tau/\mathrm{d}t(\mathbf{x}, z)$)** directly from **`18,983` live observational records** retrieved from the public **ESA Euclid DR1-Foundation (`2026`) Science Archive** (`eas.esac.esa.int/tap-server/tap/sync`, schema `dr1.*`: `11,383` VIS mosaic footprint tiles, `1,500` NISP emission-line spectra across `359` unique spectroscopic galaxies, `5,500` Wide + Deep + EDFN galaxies yielding `5,601` unique galaxies including `524` massive foreground lenses, and `600` NISP quasar records across `354` unique QSO cosmic-web tracers, totaling `5,955` unique 3D-mapped extragalactic objects across $0.064 \le z \le 5.475$), combined with multi-telescope benchmark catalogs (`Planck PR3`, `Euclid ERO Abell 2390`, `CLASH-20`, `X-COP-12`, `LoCuSS-41`, `CCCP-26`, `SPT-WTG-19`, `HSC-XXL-43`, `JWST+HST`, `JWST+ALMA`, `SLACS-70`, `TDCOSMO-7`, `SPARC-175`, `Gaia DR3`, and `NANOGrav 15-yr`).

Under the canonical, source-frozen, zero-free-parameter ($k = 0$) **Tau Core (`v19`)** terminal invariants (`H0 = 67.36 km/s/Mpc`, `Omega_b0 = 0.0493`, `Omega_m0 = 0.3153`):
- $\alpha_{\mathrm{OCSR}} = \frac{5\sqrt{3}}{24} \approx 0.36084392$, $c_{\mathrm{proj}} = \frac{1}{2}$, $c_{\mathrm{mix}} = \frac{1}{4 + \sqrt{3}} \approx 0.17445763$, $\hat{m}_{\mathrm{eff}} \approx 2.12054781$,
- Kinematic horizon scale $a_0^{\mathrm{Kin}}(z) = \frac{5\sqrt{3}}{48} c H(z)$ with $a_0^{\mathrm{Kin}}(0) = 1.180760 \times 10^{-10}\;\mathrm{m/s^2}$, and Kodama–Hayward apparent-horizon scale $a_0^{\mathrm{KH}}(z) = \frac{5\sqrt{3}}{48} c H(z)\left|1 - \frac{3}{4}\Omega_m(z)\right|$ with $a_0^{\mathrm{KH}}(0) = 0.901540 \times 10^{-10}\;\mathrm{m/s^2}$,
- $\frac{\Omega_{A,\mathrm{eff}}}{\Omega_b} = \frac{2}{\alpha_{\mathrm{OCSR}}} - c_{\mathrm{mix}} = \frac{213\sqrt{3} - 20}{65} \approx 5.36810495$ ($0.059\sigma$ parity with `Planck PR3` $\Omega_{\mathrm{DM}}/\Omega_b = 5.364 \pm 0.065$, algebraically locked via Chung Laplacian projector superselection `Theorem U1/F1`),
- $\frac{a_0^{\mathrm{KH}}(z)}{a_0^{\mathrm{KH}}(0)} = E(z)\,\frac{|1 - \frac{3}{4}\Omega_m(z)|}{|1 - \frac{3}{4}\Omega_{m,0}|}$ (`Theorem U2/F2` exterior 2-form holonomy $dK$) with exact inflection minimum at $z_{\mathrm{dip}} = \left(\frac{2\Omega_{\Lambda,0}}{\Omega_{m,0}}\right)^{1/3} - 1 = 0.6315565 \approx 0.6316$, where $a_0^{\mathrm{KH}}(z_{\mathrm{dip}})/a_0^{\mathrm{KH}}(0) = 0.9385503$,

the package demonstrates with zero ad-hoc fudge factors that:
1. **Clock Valleys ($\mathrm{d}\tau/\mathrm{d}t < 1$, apparent "dark matter"):** In live Euclid DR1 spectroscopic galaxies (median $R_{\mathrm{eff}} = 3.824\;\mathrm{kpc}$, median $g_{\mathrm{bar}}(R_{\mathrm{eff}}) = 6.7059 \times 10^{-11}\;\mathrm{m/s^2} = 0.5679\,a_0^{\mathrm{Kin}}(0) = 0.7438\,a_0^{\mathrm{KH}}(0)$), the canonical `OCSR-H1 + COCA-H1` boost law $F_{\mathrm{OD}}(R,z)$ produces a median $1.3247\times$ circular-velocity boost over pure Baryonic GR ($114.09\;\mathrm{km/s}$ vs. $84.76\;\mathrm{km/s}$; $1.3832\times$ across all `5,601` galaxies). Around `524` real Euclid DR1 massive foreground lenses, cylindrical 2D Shapiro projection yields $\Delta\Sigma_{\mathrm{Tau}}(200\;\mathrm{kpc}) = 4.0167\;M_\odot/\mathrm{pc}^2$ ($9.36\times$ boost over pure Baryonic GR $0.4292\;M_\odot/\mathrm{pc}^2$) for isolated `OCSR+COCA` and $18.0763\;M_\odot/\mathrm{pc}^2$ ($42.11\times$ boost over GR) including the two-sector condensate, while `665` overdense filament/cluster objects exhibit clock retardation below $-5\;\mathrm{ppm}$ (5th percentile $-11.09\;\mathrm{ppm}$, deepest $-289.60\;\mathrm{ppm}$).
2. **Clock Hills ($\mathrm{d}\tau/\mathrm{d}t > 1$, apparent "dark energy"):** Evaluating the exact $k = 0$ cosmological Poisson + internal galactic clock potential across `5,955` unique Euclid DR1 objects, `2,859` reside in positive-clock void domains (`1,348` in prominent voids $> +5\;\mathrm{ppm}$, 95th percentile $+35.81\;\mathrm{ppm}$, peak $+484.04\;\mathrm{ppm}$), while in the `Eridanus Supervoid` ($z = 0.15$) the $+55.69\;\mathrm{ppm}$ central Poisson clock speedup and unscreened $(1 + \Omega_A/\Omega_b) = 6.3681$ susceptibility yield $\Delta T_{\mathrm{Tau}}(0) = -153.79\;\mu\mathrm{K}$ ($\chi^2/N = 0.46$ vs. linear $\Lambda\mathrm{CDM}$ ISW $-24.15\;\mu\mathrm{K}$), resolving the `Planck CMB Cold Spot` anomaly.

## Does not claim

Following the central Tau Core AI Knowledge Base claim-boundary discipline (`.tau-core-kb/CLAIM_BOUNDARIES.md`):
- **Upstream parent selection remains open (`NATURE_LEVEL_CLOSURE = false`):** While `Theorem U1/F1` closes the internal `C1/C2` norm bifurcation via the Chung Laplacian and all terminal astrophysical equations operate at $k = 0$, the irreducible ontic existence axiom `EAS-SNPR-N1` (why an occupied $\nu = \pm 1$ observer-source sector exists rather than the recordless $\nu = 0$ algebra) keeps `NATURE_LEVEL_CLOSURE = false`.
- **QSO geometric cosmic-web tracer disclosure:** The `600` live NISP quasar emission-line records (`354` unique QSOs) lack PHZ host stellar masses and VIS Sérsic radii in the AGN catalog and are treated strictly as pure geometric cosmic-web tracers ($\Phi_{\mathrm{gal}} = 0$).
- **Low-mass group gas-evacuation boundary ($T_X < 2.5\;\mathrm{keV}$):** In low-mass galaxy groups (`HSC-XXL` low-mass subset, $N = 13$), strong AGN feedback evacuates baryonic gas beyond $R_{500}$ ($Y_b^{\mathrm{obs}} \approx 0.433$), so applying the massive-cluster shock-containment boundary ($u_{\mathrm{sh}} = 1.35\,R_{200}$) underpredicts low-mass group masses (median $M_{\mathrm{Tau}}/M_{\mathrm{WL}} = 0.679$).
- **Linear CMB degeneracy:** On the `Planck Plik_lite` `613x613` covariance matrix, Tau Core ($k_{\mathrm{DM}} = 0$) and $\Lambda\mathrm{CDM}$ ($k_{\mathrm{DM}} = 1$) are in statistical parity ($\Delta\chi^2 = +0.009$); decisive falsification resides at the late-time $z_{\mathrm{dip}} = 0.6316$ inflection point and in supervoid clock acceleration.

## Included data

All compact derived catalogs and validation summaries are stored in `data/derived/`:
- `euclid_dr1_footprint_tiles.csv` (`11,383` live Euclid DR1 VIS mosaic tiles)
- `euclid_dr1_spectroscopic_galaxies_live.csv` (`1,500` live NISP emission-line spectra across `359` unique galaxies)
- `euclid_dr1_wide_and_deep_galaxies_live.csv` (`5,500` live Wide + Deep + EDFN galaxies, including `524` massive foreground lenses)
- `euclid_dr1_quasars_live.csv` (`600` live NISP spectroscopic quasar records across `354` unique QSOs)
- `euclid_dr1_live_time_landscape_catalog.csv` (`5,955` unique 3D-mapped Euclid DR1 objects with exact $k = 0$ $\Delta(\mathrm{d}\tau/\mathrm{d}t)$ [ppm])
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
1. Regenerates the compact derived summaries, 7 English figures (`figures/` & `paper20_submission_source/figures/`), and 7 Hungarian figures (`paper20_hungarian_source/figures/`) at `300 DPI` (`scripts/generate_paper20_figures_and_summaries.py`),
2. Compiles `paper20_submission_source/main.tex` to `paper20_submission_source/main.pdf` and `paper20_hungarian_source/main.tex` to `paper20_hungarian_source/main.pdf`,
3. Builds `arxiv_submission_source.zip` (`scripts/build_arxiv_source.py`),
4. Runs the automated verification test suite (`pytest -q`), and
5. Prints `PAPER20_EUCLID_TIME_LANDSCAPE_REPRODUCTION_COMPLETE`.

## arXiv source package

- English submission source: `paper20_submission_source/` (`main.tex`, `refs.bib`, 100% English `figures/`, compiled `main.pdf`)
- Hungarian companion source: `paper20_hungarian_source/` (`main.tex`, `refs.bib`, 100% Hungarian `figures/`, compiled `main.pdf`)
- Source-only archive: `arxiv_submission_source.zip`

## Scope

Empirical multi-telescope validation and 3D cosmic time-landscape cartography under the canonical source-frozen `v19` ($k = 0$) terminal readout invariants, paired with explicit upstream claim boundaries and pre-registered Euclid DR2/DR3 & SKA falsification gates.
