/-
Wiki page: wiki/lemmas/cancellation-law.md
ID: lemma-left-cancellation
-/

import AutoProof.Definitions.Group

namespace AutoProof
namespace MyGroup

variable {G : Type} [MyGroup G]

theorem left_cancel (a b c : G) (h : mul a b = mul a c) : b = c := by
  have h1 : mul (inv a) (mul a b) = mul (inv a) (mul a c) := congrArg (mul (inv a)) h
  simp only [← mul_assoc, mul_left_inv, mul_left_id] at h1
  exact h1

theorem right_cancel (a b c : G) (h : mul b a = mul c a) : b = c := by
  have h1 : mul (mul b a) (inv a) = mul (mul c a) (inv a) := congrArg (· ⊙ inv a) h
  simp only [mul_assoc, mul_right_inv, mul_right_id] at h1
  exact h1

end MyGroup
end AutoProof
