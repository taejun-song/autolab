import Lake
open Lake DSL

package autoproof where
  leanOptions := #[⟨`autoImplicit, false⟩]

@[default_target]
lean_lib AutoProof where
  srcDir := "."
