/-
Wiki page: wiki/theorems/uniqueness-of-identity.md
ID: theorem-unique-identity
-/

import AutoProof.Definitions.Group

namespace AutoProof
namespace MyGroup

variable {G : Type} [MyGroup G]

theorem unique_identity (e' : G) (h : ∀ (a : G), mul e' a = a) : e' = e := by
  have := h e
  rw [mul_right_id] at this
  exact this

end MyGroup
end AutoProof
