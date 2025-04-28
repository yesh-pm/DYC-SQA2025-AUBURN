import hashlib

CWE_MAP = {
  "hardcoded_secret": "CWE-798",
  "exposed_network_policy": "CWE-200",
  "misconfigured_service_reference": "CWE-706"
}

def reconstruct_taint_chain(valid_taints):
  chain = []
    for inceptor, affected_file in valid_taints:
        chain.append(f"{inceptor} -> {affected_file}")
    return chain

def get_cwe_for_weakness(weakness_type):
    return CWE_MAP.get(weakness_type, "Unknown CWE")

def get_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def assess_severity(weakness_type):
    if weakness_type == "hardcoded_secret":
        return "High", "Confidentiality Impact"
    elif weakness_type == "exposed_network_policy":
        return "Medium", "Confidentiality + Availability Impact"
    else:
        return "Low", "Minimal Impact"
