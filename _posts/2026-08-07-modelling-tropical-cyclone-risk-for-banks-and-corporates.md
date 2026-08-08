---
title: "Modelling Tropical Cyclone Risk for Banks, Corporates and Regulatory Reporting: A Look Inside the Leading Platforms"
date: 2026-08-07
categories: [Climate Risk, Physical Risk, Tropical Cyclone]
---
Tropical cyclones are the costliest natural peril on the planet — a single landfalling storm can generate tens of billions of dollars in insured and uninsured losses within days. For decades, quantifying that risk was the job of a handful of catastrophe modelling firms serving (re)insurers. That has changed. Banks assessing mortgage and corporate loan books, asset managers pricing climate risk into portfolios, and corporates responding to mandatory disclosure regimes (TCFD, ISSB/IFRS S2, EU CSRD) now all need the same thing insurers have used for years: a defensible, forward-looking estimate of tropical cyclone risk at the level of an individual asset.

This post walks through how that risk is actually modelled, and who the main platforms are that banks and corporates are turning to.

<figure>
<svg viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hazard to financial loss modelling chain">
  <defs>
    <marker id="arrow1" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#1de7f5"></path>
    </marker>
  </defs>
  <style>
    .step-box { fill: #454e56; stroke: #1de7f5; stroke-width: 1.5; }
    .step-title { fill: #1de7f5; font: 700 15px 'Poppins', sans-serif; }
    .step-sub { fill: #dbe1e8; font: 400 12px 'Poppins', sans-serif; }
    .lbl { fill: #b2becd; font: 400 11px 'Poppins', sans-serif; }
  </style>

  <rect x="20" y="60" width="180" height="100" rx="12" class="step-box"></rect>
  <text x="110" y="100" text-anchor="middle" class="step-title">Hazard</text>
  <text x="110" y="122" text-anchor="middle" class="step-sub">Stochastic event set:</text>
  <text x="110" y="140" text-anchor="middle" class="step-sub">wind field, storm surge,</text>
  <text x="110" y="158" text-anchor="middle" class="step-sub">rainfall-driven flood</text>

  <line x1="200" y1="110" x2="240" y2="110" stroke="#1de7f5" stroke-width="2" marker-end="url(#arrow1)"></line>

  <rect x="245" y="60" width="180" height="100" rx="12" class="step-box"></rect>
  <text x="335" y="100" text-anchor="middle" class="step-title">Exposure</text>
  <text x="335" y="122" text-anchor="middle" class="step-sub">Asset location,</text>
  <text x="335" y="140" text-anchor="middle" class="step-sub">value, occupancy,</text>
  <text x="335" y="158" text-anchor="middle" class="step-sub">construction type</text>

  <line x1="425" y1="110" x2="465" y2="110" stroke="#1de7f5" stroke-width="2" marker-end="url(#arrow1)"></line>

  <rect x="470" y="60" width="180" height="100" rx="12" class="step-box"></rect>
  <text x="560" y="100" text-anchor="middle" class="step-title">Vulnerability</text>
  <text x="560" y="122" text-anchor="middle" class="step-sub">Damage functions:</text>
  <text x="560" y="140" text-anchor="middle" class="step-sub">hazard intensity &#8594;</text>
  <text x="560" y="158" text-anchor="middle" class="step-sub">% damage / downtime</text>

  <line x1="650" y1="110" x2="690" y2="110" stroke="#1de7f5" stroke-width="2" marker-end="url(#arrow1)"></line>

  <rect x="695" y="60" width="180" height="100" rx="12" class="step-box"></rect>
  <text x="785" y="100" text-anchor="middle" class="step-title">Financial Loss</text>
  <text x="785" y="122" text-anchor="middle" class="step-sub">AAL, VaR, PML,</text>
  <text x="785" y="140" text-anchor="middle" class="step-sub">across current climate</text>
  <text x="785" y="158" text-anchor="middle" class="step-sub">and future scenarios</text>

  <text x="450" y="205" text-anchor="middle" class="lbl">Every physical-risk platform below is a different implementation of this same four-stage chain.</text>
</svg>
<figcaption>The core modelling chain behind every tropical cyclone physical-risk platform: hazard, exposure, vulnerability, and the financial loss metrics it produces.</figcaption>
</figure>

## Why banks and corporates need this now

Three forces are pushing tropical cyclone modelling out of the reinsurance back office and into the risk functions of banks and corporates:

- **Prudential and disclosure regulation.** Climate stress tests from central banks (ECB, Bank of England, MAS) and disclosure frameworks under ISSB/IFRS S2 and CSRD require forward-looking, scenario-based physical risk metrics — not just historical loss experience.
- **Credit and real asset exposure.** Mortgage books, project finance, and REIT portfolios concentrated on hurricane-exposed coastlines (US Gulf and Atlantic coast, Caribbean, East Asia) carry collateral risk that wasn't priced into legacy underwriting.
- **Corporate resilience planning.** Multinationals with manufacturing, logistics, or data centre assets in cyclone-prone regions need site-level risk scores to prioritise capital expenditure on resilience.

## What the leading platforms are actually doing

### MSCI — Physical Risk Solutions, boosted by the First Street acquisition

MSCI's physical risk offering estimates asset-level damage under current and projected climate scenarios (including 1-in-200-year tropical cyclone events out to 2050) across large listed-company portfolios. In June 2026, MSCI announced it would acquire **First Street**, a provider of physics-based, AI-native catastrophe models validated against observed losses, covering more than 2 billion structures globally. The acquisition is explicitly aimed at giving asset owners and asset managers quantified, location-level physical risk — extending MSCI's climate analytics from portfolio-level scores toward the asset-level granularity that lenders and insurers have long used internally.

### Climate X — Spectra

Climate X's Spectra platform models 12 physical hazards, including tropical cyclones, storm surge, and coastal/surface/river flooding, built on downscaled CMIP5/CMIP6 climate projections combined with proprietary, in-house vulnerability datasets. Spectra is aimed squarely at financial institutions — the company reports it is used by banks and asset managers representing over $13.5 trillion in combined AUM — and translates hazard exposure directly into OpEx, CapEx, and revenue-at-risk metrics rather than stopping at a hazard score.

### Munich Re Risk Management Partners — Location Risk Intelligence (NATHAN)

Munich Re's **NATHAN** (Natural Hazards Assessment Network) has underpinned the reinsurer's own underwriting for decades and is now packaged as a commercial **Location Risk Intelligence** platform for insurers, banks, developers and corporate risk managers. It scores 15 natural hazards, including tropical cyclone, storm surge, and flood, and its tropical cyclone risk zoning is complemented by forward-looking projections built on the HiFLOR model (developed with NOAA GFDL) across current, 2030, 2050 and 2100 horizons under RCP 4.5 and RCP 8.5 scenarios.

### Moody's RMS and Verisk — the insurance-grade incumbents, now serving a wider market

**Moody's RMS** and **Verisk** built the stochastic cyclone/hurricane/typhoon models the (re)insurance industry has relied on for over 30 years, calibrated against decades of insurance claims and post-event damage surveys. Verisk's 2026 release of a reengineered US Tropical Cyclone Model — delivered on its new Synergy Studio platform — moved to a single "near-present" view of hurricane risk that blends global warming signals with natural Atlantic basin variability, alongside an updated vulnerability model for storm surge and rainfall-driven inland flood. Both vendors are increasingly packaging this same underlying science for non-insurance buyers — banks, corporates, and capital markets participants — who need the same rigor insurers have always demanded.

<div class="table-wrap">
<table>
<thead>
<tr><th>Platform</th><th>Origin / core strength</th><th>Peril breadth</th><th>Primary buyer today</th></tr>
</thead>
<tbody>
<tr><td>MSCI + First Street</td><td>Portfolio climate analytics + AI-native physics-based hazard data</td><td>Multi-hazard, 2B+ structures globally</td><td>Asset owners, asset managers, banks</td></tr>
<tr><td>Climate X (Spectra)</td><td>In-house climate science built for financial services</td><td>12 hazards incl. TC, surge, flood, wildfire</td><td>Banks, insurers, asset managers</td></tr>
<tr><td>Munich Re RMP (NATHAN)</td><td>40 years of reinsurer-grade hazard data</td><td>15 hazards, TC zoning + HiFLOR projections</td><td>Insurers, banks, developers, corporates</td></tr>
<tr><td>Moody's RMS</td><td>Insurance-grade stochastic cat models</td><td>Cyclone/hurricane/typhoon, HD model suite</td><td>(Re)insurers, increasingly banks/investors</td></tr>
<tr><td>Verisk</td><td>Claims-validated vulnerability + new Synergy Studio platform</td><td>Reengineered US TC model (2026)</td><td>(Re)insurers, capital markets, corporates</td></tr>
</tbody>
</table>
</div>

## What to actually compare

When evaluating any of these platforms, the marketing language ("AI-powered," "physics-based," "climate-validated") converges quickly — the differentiators that matter in practice are:

1. **Granularity** — asset-level (single building/coordinate) versus regional/postcode-level scoring.
2. **Scenario coverage** — which emissions pathways (RCP/SSP) and time horizons are supported, and whether outputs map cleanly to disclosure requirements.
3. **Validation** — how the vulnerability functions were calibrated: against real insurance claims and post-event surveys, or purely modelled.
4. **Financial translation** — whether the platform stops at a hazard score, or converts hazard + vulnerability into loss, VaR, or business-interruption metrics a CFO can use directly.

<div class="callout">
<strong>Why this matters for parametric insurance.</strong> The same hazard science described above — stochastic event sets, wind field intensity, storm surge — is exactly what underpins the index used to trigger a parametric payout. Understanding how the risk is <em>modelled</em> is the first half of the picture; how it gets <em>transferred</em> is the second. That's the subject of the next post.
</div>

Subscribe below to get that post — and future notes on physical climate risk and catastrophe modelling — as soon as they're published.

Sources: [MSCI Physical Risk Solutions](https://www.msci.com/data-and-analytics/climate-solutions/physical-risk-solutions) · [MSCI acquires First Street](https://www.msci.com/discover-msci/media-room/msci-acquires-first-street-to-enhance-physical-climate-risk-capabilities-for-financial-decision-making) · [Climate X Spectra](https://www.climate-x.com/spectra) · [Climate X Spectra methodology](https://www.climate-x.com/spectra/methodology) · [Munich Re RMP Location Risk Intelligence](https://www.munichre.com/rmp/en/products/location-risk-intelligence.html) · [Munich Re NATHAN, Natural Hazards Edition](https://www.munichre.com/rmp/en/products/location-risk-intelligence/natural-hazards-edition.html) · [Moody's RMS cyclone/hurricane/typhoon models](https://www.rms.com/models/cyclone-hurricane-typhoon) · [Verisk Tropical Cyclone Model / Synergy Studio](https://www.verisk.com/company/newsroom/verisk-redefines-u.s.-hurricane-risk-modeling-with-reengineered-tropical-cyclone-model-delivered-on-its-new-synergy-studio-platform/)
