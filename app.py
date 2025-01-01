from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/gst-status', methods=['GET'])
def get_gst_status():
    # Extract the 'gst_number' and 'month' parameters from the URL
    gst_number = request.args.get('gst_number')
    month = request.args.get('month')

    if not gst_number or not month:
        return jsonify({"error": "Please provide both gst_number and month"}), 400
    
    # Logic to fetch the GST status (this is a placeholder - replace it with your actual logic)
    gst_status = {
        "gst_number": gst_number,
        "month": month,
        "status": "Filed",  # Replace with actual logic
        "return_details": "Details of the GST return for this month."
    }
    
    # Return the response as JSON
    return jsonify(gst_status)


# For production deployment, use Gunicorn as the server
if __name__ == "__main__":
    app.run(debug=True)
