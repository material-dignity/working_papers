# Contributing to Material Dignity Infrastructure

This repository contains five working papers that specify a structural framework for reversing chronic unsheltered homelessness. Four papers are published on SSRN. The fifth paper is in development. All are maintained here as living documents and open to contribution.

## What This Project Is

Material Dignity Infrastructure is a five-paper theoretical architecture covering the full street-to-sovereignty pipeline:

- **WP1**: Material Dignity Infrastructure (physical stabilization)
- **WP2**: Structural Misalignment (activation of surplus shelter capacity)
- **WP3**: Los Angeles Metropolitan Stabilization (street-to-home pipeline analysis)
- **WP4**: Relational Dignity Infrastructure (the human layer)
- **WP5**: Economic Dignity Infrastructure (cooperative reintegration and labor market reentry) [Draft]

The papers specify mechanisms. They do not yet contain implementation data, financial projections at unit level, or site-specific adaptation guides. That work requires more minds than one. We explicitly invite data scientists, urban architects, and econometricians to audit the falsifiable claims made throughout the framework and contribute data to close these gaps.

## Where Contributions Are Needed

The following gaps are open and named. Each represents a self-contained contribution opportunity. You do not need to read all five papers to contribute to one section.

### Financial Modeling

WP5 specifies the Tenancy Bridge Guarantee and Cooperative Reintegration Mechanism at the categorical level. Unit-level financial projections are needed:

- CalAIM reimbursement rate modeling by county (California)
- Oregon CCO and Washington State Medicaid waiver equivalents
- Cooperative enterprise revenue projections at 50, 100, and 150 resident enrollment
- Operating gap analysis under variable Medicaid rate scenarios
- Master lease cost modeling by metro market

### Legal and Regulatory

- Model cooperative bylaws for resident-worker ownership within a supportive housing context
- CalAIM billing compliance documentation for Housing Transition Navigation Services
- Zoning and land use analysis for congregate cooperative housing in target municipalities
- Liability framework for peer-led security operations within cooperative governance

### Implementation and Case Studies

- Existing cooperative housing models that approximate the MDI architecture (domestic or international)
- IPS (Individual Placement and Support) integration case studies within residential settings
- Pod Steward role analogues in existing peer support or therapeutic community models
- Transition outcome data from programs that bridge supportive housing to independent tenancy

### Clinical and Evaluation Design

- Psychometric instrument selection and validation for identity capital measurement
- Longitudinal evaluation design for a 24-36 month pilot
- Leading indicator calibration (what thresholds on the 12-month metrics predict 36-month outcomes)
- Return Deficit index construction and measurement methodology

### Policy and Comparative Analysis

- International social cooperative frameworks (Italian Type B cooperatives, UK social enterprises)
- Comparative Medicaid waiver structures across states with housing-related Community Supports
- Political economy of municipal implementation (council approval, NIMBY mitigation, provider contracting)

### Technical Infrastructure

- Data systems for cooperative labor logging, governance participation tracking, and psychometric administration
- Automated CalAIM billing integration
- Resident-facing tools for tracking identity capital accumulation and transition readiness

## How to Contribute

**Fork and pull request.** The standard open-source workflow applies. Fork this repository, make your contribution, and submit a pull request with a clear description of what you are adding and which gap it addresses.

**File placement.** Contributions to existing papers go in the relevant working paper directory under a `contributions/` subfolder. New analyses, models, or case studies that stand alone go in a top-level `contributions/` directory with a descriptive filename.

**Format.** Markdown for text. LaTeX for formal modeling. Python or R for computational work. PDF only as a compiled output, never as a sole source.

**Citation.** If your contribution references external literature, use the same citation format as the existing papers (author-year in brackets, full reference at end). If your contribution is substantial enough to warrant independent citation, include a suggested citation line at the top.

**Scope.** Contributions should extend, stress-test, or operationalize the existing architecture. This is not a general homelessness research repository. Contributions that contradict the framework's premises are welcome if they bring evidence; contributions that propose alternative frameworks belong in their own repositories.

## What Happens to Contributions

Accepted pull requests are merged into the working repository. Contributors are credited in a CONTRIBUTORS.md file with their name (or handle), area of contribution, and date. Substantial contributions that alter the theoretical architecture will be acknowledged in subsequent paper revisions on SSRN.

**Decisions are made via open-source consensus.** Per the [GOVERNANCE.md](./GOVERNANCE.md) protocol, this ensures that technical direction is driven by data validation and empirical verification. The Principal Systems Architect retains ultimate authority over the engineering core, ensuring your voice is heard and integrated via a generic administrative Git account without requiring public exposure.

This is not an academic journal. There is no traditional peer review gate; there is rigorous engineering judgment regarding coherence, falsifiability, and quality. If a contribution is rejected, the empirical or logical reason will be stated in the pull request discussion.

## Who Should Contribute

- Economists with experience in labor market modeling, cooperative economics, or Medicaid financing
- Social workers and clinicians with implementation experience in supportive housing or IPS
- Legal professionals with expertise in cooperative law, Medicaid compliance, or municipal zoning
- Researchers with longitudinal evaluation design experience
- Policy analysts working in housing, homelessness, or workforce development
- Engineers building data systems for social service delivery
- Anyone with direct lived experience of the systems these papers describe

## Contact

Open an issue on this repository. That is the primary channel. No email. No DMs. Public discussion produces public knowledge.
