import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to fetch GST return status
@app.route('/api/gst-status', methods=['GET'])
def gst_status():
    gstin = request.args.get('gst_number')
    month = request.args.get('month')
    year = request.args.get('year')  # Add this to support fy (financial year)
    return_type = request.args.get('type', 'monthly')  # Default to monthly

    # Construct the GST API URL
    gst_api_url = f"https://developer.gst.gov.in/apiportal/commonapi/v1.0/returns?gstin={gstin}&fy={year}&type={return_type}"

    # Headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with the actual API key if required
    }

    # Send the request to the GST API
    response = requests.get(gst_api_url, headers=headers)

    if response.status_code == 200:
        # Return the actual GST API response
        return jsonify(response.json())
    else:
        # Handle errors and return appropriate messages
        return jsonify({"error": "Failed to fetch GST return status", "status_code": response.status_code}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
