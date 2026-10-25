# Ex. No. : 4 - NETWORK TRAFFIC ANALYSIS
# AIM: To capture, monitor, and analyze the network traffic using mitmproxy.

from mitmproxy import http


def request(flow: http.HTTPFlow):
    print("====================================")
    print("Request URL :", flow.request.pretty_url)
    print("Request Method :", flow.request.method)
    print("Client IP :", flow.client_conn.address)
    print("====================================")


def response(flow: http.HTTPFlow):
    print("Status Code :", flow.response.status_code)
    print("Content Type :", flow.response.headers.get("Content-Type"))
