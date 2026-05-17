/-
Wiki page: wiki/definitions/group-structure.md
ID: definition-group
-/

namespace AutoProof

class MyGroup (G : Type) where
  mul : G → G → G
  e : G
  inv : G → G
  mul_assoc : ∀ (a b c : G), mul (mul a b) c = mul a (mul b c)
  mul_left_id : ∀ (a : G), mul e a = a
  mul_right_id : ∀ (a : G), mul a e = a
  mul_left_inv : ∀ (a : G), mul (inv a) a = e
  mul_right_inv : ∀ (a : G), mul a (inv a) = e

namespace MyGroup

variable {G : Type} [MyGroup G]

infixl:70 " ⊙ " => MyGroup.mul

end MyGroup

end AutoProof
