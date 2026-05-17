/-
Wiki page: wiki/examples/contradiction-idempotent-identity.md
ID: example-contradiction-proof
-/

import AutoProof.Definitions.Group
import AutoProof.Lemmas.CancellationLaw

namespace AutoProof
namespace MyGroup

variable {G : Type} [MyGroup G]

theorem idempotent_is_identity (a : G) (h : mul a a = a) : a = e := by
  apply left_cancel a
  rw [h, mul_right_id]

end MyGroup
end AutoProof
