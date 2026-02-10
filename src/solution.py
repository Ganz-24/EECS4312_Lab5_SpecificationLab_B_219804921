## Student Name: Matthew Magagna
## Student ID: 219804921

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    # TODO: Implement this function

    totals: Dict[str, float] = {}

    # Validate capacities and initialize totals
    for r_name, cap in resources.items():
        if not isinstance(cap, (int, float)):
            return False
        if cap < 0:
            return False
        totals[r_name] = 0.0

    # Validate and accumulate requests
    for req in requests:
        if not isinstance(req, dict):
            raise ValueError("Each request must be a dict.")

        for r_name, amount in req.items():
            # Resource must exist
            if r_name not in resources:
                return False
            # Amount must be numeric and non-negative
            if not isinstance(amount, (int, float)):
                return False
            if amount < 0:
                return False

            totals[r_name] += float(amount)

            # Capacity must not be exceeded
            if totals[r_name] > float(resources[r_name]):
                return False

    # NEW REQUIREMENT:
    # At least one resource must remain unallocated (some capacity left over)
    # Allocation is invalid if ALL resources are fully consumed.
    for r_name, cap in resources.items():
        if totals.get(r_name, 0.0) < float(cap):
            return True

    return False
