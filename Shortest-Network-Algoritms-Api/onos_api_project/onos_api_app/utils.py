import requests

ONOS_URL = "http://localhost:8181/onos/v1"
AUTH = ('onos', 'rocks')

def get_links():
    response = requests.get(f"{ONOS_URL}/links", auth=AUTH)
    data = response.json()
    return data.get("links", [])

def build_graph_from_links(links):
    graph = {}
    for link in links:
        src = link["src"]["device"]
        dst = link["dst"]["device"]
        graph.setdefault(src, {})[dst] = 1
        graph.setdefault(dst, {})[src] = 1
    return graph
