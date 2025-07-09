from flask import render_template, send_from_directory

def setup_frontend_routes(app):
    """Set up routes for serving the frontend files"""
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/assets/<path:filename>')
    def assets(filename):
        return send_from_directory('frontend/dist/assets', filename)
