import Mathlib

/-! Schur over ℂ, using Mathlib's actual finite-dimensional representation
category. A chosen finite biproduct decomposition records semisimplicity;
no concrete Spin representation or claimed kinetic eigenvalue is assumed. -/
namespace B07Argon.Schur
open CategoryTheory CategoryTheory.Limits
open scoped BigOperators
variable {G : Type} [Monoid G]

local instance : HasFiniteBiproducts (FDRep ℂ G) :=
  HasFiniteBiproducts.of_hasFiniteProducts

theorem irreducible_scalar (V : FDRep ℂ G) [Simple V] (f : V ⟶ V) :
    ∃ c : ℂ, c • 𝟙 V = f :=
  CategoryTheory.endomorphism_simple_eq_smul_id ℂ f

theorem inequivalent_zero (V W : FDRep ℂ G) [Simple V] [Simple W]
    (h : ¬ Nonempty (V ≅ W)) (f : V ⟶ W) : f = 0 := by
  by_contra hn
  haveI : IsIso f := (CategoryTheory.isIso_iff_nonzero f).mpr hn
  exact h ⟨asIso f⟩

/-- Each entry on m equivalent copies is an independent Schur scalar, hence
the endomorphism is a full multiplicity matrix, not necessarily one scalar. -/
theorem isotypic_matrix (V : FDRep ℂ G) [Simple V] (m : ℕ)
    (f : (⨁ fun _ : Fin m => V) ⟶ (⨁ fun _ : Fin m => V)) :
    ∃ c : Fin m → Fin m → ℂ,
      biproduct.matrix (fun i j => c i j • 𝟙 V) = f := by
  have hh : ∀ i j : Fin m, ∃ c : ℂ,
      c • 𝟙 V = biproduct.ι (fun _ : Fin m => V) i ≫ f ≫ biproduct.π (fun _ : Fin m => V) j :=
    fun i j => irreducible_scalar V _
  choose c hc using hh
  refine ⟨c, ?_⟩
  simp_rw [hc]
  exact biproduct.components_matrix f

theorem multiplicity_matrix_injective (V : FDRep ℂ G) [Simple V] (m : ℕ) :
    Function.Injective (fun c : Fin m → Fin m → ℂ =>
      biproduct.matrix (fun i j => c i j • 𝟙 V)) := by
  intro c d h
  funext i j
  apply smul_left_injective ℂ (id_nonzero V)
  have hh := congrArg (fun f => biproduct.components f i j) h
  simpa using hh

/-- General semisimple decomposition: inequivalent entries are zero.
Equivalent repeated summands are handled by isotypic_matrix. -/
theorem semisimple_off_isotypic_zero {ι : Type} [Fintype ι]
    (V : ι → FDRep ℂ G) [∀ i, Simple (V i)]
    (f : (⨁ V) ⟶ (⨁ V)) (i j : ι) (h : ¬ Nonempty (V i ≅ V j)) :
    biproduct.ι V i ≫ f ≫ biproduct.π V j = 0 :=
  inequivalent_zero (V i) (V j) h _

theorem multiplicity_one_summand {ι : Type} [Fintype ι] [DecidableEq ι]
    (V : ι → FDRep ℂ G) [∀ i, Simple (V i)]
    (f : (⨁ V) ⟶ (⨁ V)) (i : ι)
    (hm : ∀ j, i ≠ j → ¬ Nonempty (V i ≅ V j)) :
    ∃ c : ℂ, biproduct.ι V i ≫ f = c • biproduct.ι V i := by
  obtain ⟨c, hc⟩ := irreducible_scalar (V i) (biproduct.ι V i ≫ f ≫ biproduct.π V i)
  refine ⟨c, ?_⟩
  apply biproduct.hom_ext
  intro j
  by_cases hij : i = j
  · subst j
    simpa using hc.symm
  · rw [Category.assoc, semisimple_off_isotypic_zero V f i j (hm j hij)]
    simp [hij]

end B07Argon.Schur
