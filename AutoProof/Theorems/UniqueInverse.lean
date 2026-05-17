/-
Wiki page: wiki/theorems/uniqueness-of-inverse.md
ID: theorem-unique-inverse
-/

import AutoProof.Definitions.Group
import AutoProof.Lemmas.CancellationLaw

namespace AutoProof
namespace MyGroup

variable {G : Type} [MyGroup G]

theorem unique_inverse (a b : G) (h : mul a b = e) : b = inv a := by
  apply left_cancel a
  rw [h, mul_right_inv]

end MyGroup
end AutoProof
