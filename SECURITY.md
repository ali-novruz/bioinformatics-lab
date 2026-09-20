# Security policy

## Reporting a vulnerability

Do not publish credentials, private biological data, or an exploitable security issue in a public GitHub issue. Use GitHub's **Security → Report a vulnerability** flow for this repository and include the affected version, a minimal reproduction, expected impact, and any safe mitigation you tested.

Routine correctness bugs, documentation errors, and non-sensitive reproducibility problems may use the public issue templates.

## Supported version

Security fixes target the current `main` branch and the latest tagged release. This educational repository does not process protected health information and is not a clinical system.

Never commit API keys, access tokens, patient identifiers, controlled cohort data, or unrestricted raw data. Follow [DATA_POLICY.md](DATA_POLICY.md) and remove sensitive material from Git history before sharing a branch.
