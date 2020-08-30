from flask import Blueprint, request, jsonify, Response, redirect, abort
from .url import Url
from datetime import datetime

urls = Blueprint('urls', __name__)

@urls.route('/short', methods=['POST'])
def create_short_url():
    data = request.get_json()
    original_url = data.get('originalUrl')
    url = Url.objects(original_url=original_url).first()
    if url is None:
        url = Url(original_url=original_url, created_at=datetime.now())
        url.save()
        url.short_url = str(url.id)[-7:]
        url.save()
    
    return jsonify(url.short_url)

@urls.route('/<short_url>', methods=['GET'])
def get_original_url(short_url):
    url = Url.objects(short_url=str(short_url)).first()
    if url is not None:
        return redirect(url.original_url)
    else:
        abort(404, description="URL not found")
