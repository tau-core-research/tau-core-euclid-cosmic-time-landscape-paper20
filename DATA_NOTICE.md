# Data Provenance and Scope Notice (Paper 20)

This repository contains the reproducibility package for **Paper 20** (`tau-core-euclid-cosmic-time-landscape-paper20`):
*The Cosmic Time-Landscape ($M_\tau^\star$): Live ESA Euclid DR1-Foundation Validation and Multi-Telescope Atlas of the Zero-Parameter Tau Core Universe Model*.

## Included Public Observational Data Extracts (`data/derived/`)

1. **Live ESA Euclid DR1-Foundation Science Archive (`https://eas.esac.esa.int/tap-server/tap/sync`, schema `dr1.*`, `18,983` total records):**
   - `euclid_dr1_footprint_tiles.csv`: `11,383` real VIS mosaic tiles (`dr1.mosaic_product`) spanning the $1,900\;\mathrm{deg}^2$ Euclid DR1-Foundation footprint.
   - `euclid_dr1_spectroscopic_galaxies_live.csv`: `1,500` real NISP spectroscopic emission-line measurements across `359` unique galaxies ($0.1309 \le z_{\mathrm{spec}} \le 3.4927$, `spe_rank = 0`, `spe_z_prob > 0.95`, $\mathrm{SNR} > 6.0$), joined across `dr1.spectro_z_spe_galaxy_candidates_deep`, `dr1.spectro_line_features_spe_line_features_deep`, `dr1.mer_catalogue_deep_mode`, `dr1.phz_physical_parameters_deep_mode`, and `dr1.mer_morphology_deep_mode`.
   - `euclid_dr1_wide_and_deep_galaxies_live.csv`: `5,500` real galaxies across the Euclid Deep Field North (`EDFN`), `COSMOS`, Euclid Deep Field Fornax (`EDFF/CDFS`), and `Southern Wide Survey`, containing `524` massive foreground lenses ($0.15 < z_L < 0.90$, $\log_{10}(M_*/M_\odot) \ge 10.3$).
   - `euclid_dr1_quasars_live.csv`: `600` real NISP spectroscopic quasars (`0.31 <= z_spec <= 5.49`).
   - `euclid_dr1_live_time_landscape_catalog.csv`: Reconstructed 3D comoving coordinates, cosmic web overdensity $\delta_g$, local cosmic clock-rate shift $\Delta(\mathrm{d}\tau/\mathrm{d}t)$ [ppm], and effective lensing convergence $\kappa_{\mathrm{Tau}}$ across `5,955` unique live Euclid DR1 extragalactic objects.
   - `euclid_dr1_live_validation_results.json`: Complete validation summary JSON.

2. **Multi-Telescope Extragalactic & Cosmological Benchmark Catalogs (`data/derived/`):**
   - `tau_core_universe_model_catalog_v1.csv` (`249` cataloged benchmark sky structures across `Planck`, `Euclid ERO Abell 2390`, `CLASH-20`, `X-COP-12`, `LoCuSS-41`, `CCCP-26`, `SPT-WTG-19`, `HSC-XXL-43`, `JWST+HST 43`, `JWST+ALMA 17`, `JWST Ultra-High-z`, and major superclusters/supervoids).
   - `tau_core_universe_model_validation_v1.json`
   - `paper20_euclid_dr1_field_summary.csv`
   - `paper20_multi_telescope_benchmark_summary.csv`
