/-
Wiki page: wiki/examples/direct-proof-double-inverse.md
ID: example-direct-proof
-/

import AutoProof.Definitions.Group
import AutoProof.Lemmas.CancellationLaw

namespace AutoProof
namespace MyGroup

variable {G : Type} [MyGroup G]

theorem inv_inv (a : G) : inv (inv a) = a := by
  apply left_cancel (inv a)
  rw [mul_left_inv, mul_right_inv]

end MyGroup
end AutoProof
