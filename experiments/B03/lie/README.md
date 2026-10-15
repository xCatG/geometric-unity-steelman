# B03 LiE oracle

Generate the external fixture from the repository root in PowerShell:

```powershell
wsl -d Ubuntu-24.04 -- bash -lc 'lie < /mnt/c/work/src/GU/experiments/B03/lie/oracle.lie' > experiments/B03/lie/oracle.out 2> experiments/B03/lie/oracle.err
```

Write `oracle.lie` with LF line endings. Require exit 0, an empty `oracle.err`, and `END B03 ORACLE` as the last nonblank output line; remove the empty error file after checking. Preserve LiE's output bytes (LF), without hand editing.

Verified environment:

- `wsl -d Ubuntu-24.04 -- dpkg-query -W lie`: `lie 2.2.2+dfsg-3build3`.
- `wsl -d Ubuntu-24.04 -- sha256sum /usr/lib/lie/lie`: `1c0de3b4ca4e861cb00185305b161460cc4b88e473b8e4ef741055bd2439bf37`.
- `oracle.lie` SHA-256: `6a280425e393f9c77cdd7fcd063290fe1a0485b53f926d6e0ccb5f8383d903e2`.
- `oracle.out` SHA-256: `576888f244d92358a54448df4c977f64a2459fb751a0d101e6cedc5f6c9268c6`.

Dynkin labels use Bourbaki order. The D5A1A1 output order is D5, A1_L, A1_R. The D5-to-A4T1 matrix `r` reverses the A4 diagram so the chosen fundamental is the old omega4, and its U(1) charge is X, the sum of doubled orthonormal D5 coordinates. It gives `16 = 10_1 + 5bar_-3 + 1_5`.

The A2A1T1 matrix `e` has rows equal to images of the D5 fundamental weights under embedding E from the ansatz. Its target coordinates are SU(3) Dynkin labels, the SU(2) Dynkin label, and n = 6Y. Both restriction matrices are printed in the fixture, along with the dimensions, tensor products, branchings and zero residual controls.

Tests never call LiE. They read the tracked `oracle.out` with `experiments.B03.oracle`; WSL is required only for regeneration.
