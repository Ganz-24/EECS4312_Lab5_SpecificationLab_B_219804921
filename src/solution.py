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

    # Basic validity checks on capacities and initialize totals
    totals: Dict[str, float] = {}
    for r_name, cap in resources.items():
        if not isinstance(cap, (int, float)):
            return False
        if cap < 0:
            return False
        totals[r_name] = 0.0

    # Accumulate all requests and ensure we never exceed capacity
    for req in requests:
        if not isinstance(req, dict):
            return False

        for r_name, amount in req.items():
            # Requesting a resource that doesn't exist in the capacity map is infeasible
            if r_name not in resources:
                return False
            if not isinstance(amount, (int, float)):
                return False
            if amount < 0:
                return False

            totals[r_name] += float(amount)

            # Early exit if capacity is exceeded
            if totals[r_name] > float(resources[r_name]):
                return False

    return True
