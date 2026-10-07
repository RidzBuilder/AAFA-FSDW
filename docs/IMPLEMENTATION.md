# Implementation v0.1

This repository implements the first governed AAFA-FSDW Operational Kernel slice.

## Implemented
- canonical evidence levels/status;
- claim/evidence alignment;
- deterministic gate precedence;
- controlled operational transitions;
- runtime trace contract;
- decision context snapshot contract;
- authority/permission boundary;
- baseline tests.

## Deliberately not claimed
- E4/E5 runtime proof;
- AAFA conformance;
- agentic behavior of this kernel;
- production readiness;
- provider-specific semantic authority.

## Verification
Run:

    python -m pytest

The implementation follows the locked distinctions:
BUILD != PROOF
RUN != CONFORMANCE
ABSTRACTION != AGNOSTICITY
TOOLS != AGENCY
WORKFLOW != AGENT
MEMORY != AGENCY
UI != AGENCY
ADAPTER != PROOF
