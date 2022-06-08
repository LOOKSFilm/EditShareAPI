import requests
import urllib3


headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
            }



class FlowMetadata:
    """ 
    connect to EditShare Server:

    FlowMetadata("ip", "username", "password")

    FlowMetadata.connection returns "true" if connected
    """
    def __init__(self, ip, user, password) -> None:
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.server = ip
        user = user
        password = password
        self.session.auth = (user, password)
        data = [user, password]
        self.connection = self.session.post('https://'+self.server+':8006/api/v2/admin/check_password', verify=False, headers=headers, json=data).text
        
    
    def ping(self):
        ping = self.session.get("https://"+self.server+":8006/api/v2/database/ping",verify=False, headers=headers)
        return ping
#############
### ASSET ###
#############
    def addAsset(self, data):
        """ 
        Input: Data in JSON format

        Adds an asset.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/post_assets
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/assets', verify=False, headers=headers, json=data)
        return response

    def getAsset(self, asset_id, vendor_data=False):
        """ 
        Input: asset_id or uuid
        uuid has to be String

        Get AssetData Object. (.data for JSON)

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets__asset_id_
        """
        # params = (
        #     ('vendor_data', vendor_data)
        # )
        if type(asset_id) == int:
            asset_id = str(asset_id)
        try:
            response = self.session.get('https://'+self.server+':8006/api/v2/database/assets/'+asset_id, verify=False, headers=headers).json()
        except TypeError:
            print('EditShare Modul Error:\n-------------------------------------------------------------------------------------------\nID has to be String\n-------------------------------------------------------------------------------------------')
        #I AM TRYING TO RETURN AN OBJECT BUT KEYERRORS ARE ANNOYING
        # class AssetData:
        #     def __init__(self, response, asset_type, asset_type_id, asset_type_text, asset_version, comment, custom, customtypes, nle_id, origin_site, uuid):
        #         self.data = response
        #         self.asset_type = asset_type
        #         self.asset_type_id = asset_type_id
        #         self.asset_type_text = asset_type_text
        #         self.asset_version = asset_version
        #         self.comment = comment
        #         self.custom = custom
        #         self.customtypes = customtypes
        #         self.nle_id = nle_id
        #         self.origin_site = origin_site
        #         # self.thumbnail = thumbnail
        #         # self.thumbnail_path = thubnail_path
        #         self.uuid = uuid
        # assetdata = AssetData(response, response['asset_type'],response['asset_type_id'],response['asset_type_text'],response['asset_version'],response['comment'],response['custom'],response['customtypes'],response['nle_id'],response['origin_site'],response['uuid'])
        return response
    
    def updateAsset(self, asset_id, data):
        """ 
        Input: asset_id or uuid
        uuid has to be String

        Update asset Metadata.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/put_assets__asset_id_
        """
        if type(asset_id) == int:
            asset_id = str(asset_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/assets/'+asset_id, verify=False, headers=headers, data=data)
        return response
    
    def deleteAsset(self, asset_id):
        """ 
        Input: asset_id or uuid
        uuid has to be String

        Delete asset data entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/delete_assets__asset_id_
        """
        if type(asset_id) == int:
            asset_id = str(asset_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/assets/'+asset_id, verify=False, headers=headers)
        return response
    
    def getAssetVendorData(self, asset_id):
        """ 
        Input: asset_id

        Get vendor data associated with an asset.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets__asset_id__vendor_data
        """
        if type(asset_id) == int:
            asset_id = str(asset_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/assets/'+asset_id+'/vendor_data', verify=False, headers=headers).json()
        return response
    
    def getAssetAssociations(self, asset_id):
        """ 
        Input: asset_id or asset_collection_id or uuid
        uuid has to be String

        Get asset associations by id.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets__uuid__associations
        """
        if type(asset_id) == int:
            asset_id = str(asset_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/assets/'+asset_id+'/associations', verify=False, headers=headers).json()
        return response

    def associateAsset(self, asset_id, associated_asset_id):
        """ 
        Input: asset_id, asset_association_id

        Associate another asset with "this" one.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/put_assets__asset_id__associations__associated_asset_id_
        """
        if type(asset_id) == int:
            asset_id = str(asset_id)
        if type(associated_asset_id) == int:
            associated_asset_id = str(associated_asset_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/assets/'+asset_id+'/associations/'+associated_asset_id, verify=False, headers=headers).json()
        return response

    def deleteAssociation(self, asset_id, associated_asset_id):
        """ 
        Input: asset_id, asset_association_id

        Delete an asset association entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/delete_assets__asset_id__associations__associated_asset_id_
        """
        if type(asset_id) == int:
            asset_id = str(asset_id)
        if type(associated_asset_id) == int:
            associated_asset_id = str(associated_asset_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/assets/'+asset_id+'/associations/'+associated_asset_id, verify=False, headers=headers).json()
        return response

    def addAssetAssosiation(self, data):
        """ 
        Input: Data in JSON format

        Add an asset association.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/post_assets_associations
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/assets/associations', verify=False, headers=headers, data=data).json()
        return response

    def getAssetAssosiation(self, asset_collection_id):
        """ 
        Input: asset_collection_id or uuid
        uuid has to be String

        Get an asset association

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets_associations__asset_collection_id_
        """
        if type(asset_collection_id) == int:
            asset_collection_id = str(asset_collection_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/assets/associations/'+asset_collection_id, verify=False, headers=headers).json()
        return response
    def addAssetAssosiation(self, asset_collection_id):
        """ 
        Input: asset_collection_id or uuid
        uuid has to be String

        Modify an asset association, using the association's database ID.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/put_assets_associations__asset_collection_id_
        """
        if type(asset_collection_id) == int:
            asset_collection_id = str(asset_collection_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/assets/associations/'+asset_collection_id, verify=False, headers=headers).json()
        return response
    
    def deleteAssetAssosiation(self, asset_collection_id):
        """ 
        Input: asset_collection_id or uuid
        uuid has to be String

        Delete an asset association, using the association's database ID
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/delete_assets_associations__asset_collection_id_
        """
        if type(asset_collection_id) == int:
            asset_collection_id = str(asset_collection_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/assets/associations/'+asset_collection_id, verify=False, headers=headers).json()
        return response

    def exportMetadata(self, asset_id):
        params = {
            'export_format': 'xml',
            'asset_metadata': 'true',
            'asset_custom_metadata': 'true',
            'file_details': 'true',
            'location_details': 'true',
            'backup_details': 'true',
            'markers': 'true',
            'csv_framerates': 'false',
            'csv_comments': 'false',
            'csv_bom': 'false',
        }
        if type(asset_id) == int:
            asset_id = str(asset_id)
        response = self.session.get("https://"+self.server+":8006/api/v2/database/assets/"+asset_id+"/export", params=params)
        return response

###############
### CAPTURE ###
###############
    def addCapture(self, data, createcaptureonly=False):
        """ 
        Input: Data in JSON format

        Create new capture. If the cature id or recording id exists only a new chunk group is created.
        """
        params = (
            ('createcaptureonly', createcaptureonly)
        )
        response = self.session.post('https://'+self.server+':8006/api/v2/database/captures', headers=headers, data=data, params=params)
        return response

    def deleteCapture(self, capture_id):
        """ 
        Input: capture_id or uuid
        uuid has to be String

        Delete a capture entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/delete_captures__capture_id_
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        response = self.session.delete('https://'+self.server+':8006//api/v2/database/captures/'+capture_id, verify=False, headers=headers)
        return response

    def getCapture(self, capture_id):
        """ 
        Input: capture_id

        Get details about capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id_
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/captures/'+capture_id, verify=False, headers=headers)
        return response

    def updateCapture(self, capture_id, data):
        """ 
        Input: capture_id, Data in JSON format

        Update capture data.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/put_captures__capture_id_
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/captures/'+capture_id, verify=False, headers=headers, data=data)
        return response

    def getCaptureClips(self, capture_id):
        """ 
        Input: capture_id

        Get Clips in a capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id__clips
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/captures/'+capture_id+'/clips', verify=False, headers=headers)
        return response

    def getChunkGroup(self, capture_id):
        """ 
        Input: capture_id

        Get chunk groups in capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id__groups
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/captures/'+capture_id+'/groups', verify=False, headers=headers)
        return response

    def getChunkGroupClips(self, capture_id, chunk_group_id):
        """ 
        Input: capture_id, chunk_group_id

        Get the clips in the specified chunk group for a particular capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id__groups__chunk_group_id_
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        if type(chunk_group_id) == int:
            chunk_group_id = str(chunk_group_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/captures/'+capture_id+'/groups/'+chunk_group_id, verify=False, headers=headers)
        return response

    def deleteCaptureLogEntries(self, capture_id, log_entry_sources='user,qc,ingest,import,audio_metadata,video_metadata,review_approve'):
        """ 
        Input: capture_id

        Delete all the log entries for a capture. You can specify a uuid or id, and limit to a type (or types) of log entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/delete_captures__capture_id__log_entries
        """
        if type(capture_id) == int:
            capture_id = str(capture_id)
        params = (
            ('log entry sources', log_entry_sources)
        )
        response = self.session.get('https://'+self.server+':8006/api/v2/database/captures/'+capture_id+'/log_entries', verify=False, headers=headers, params=params)
        return response

#############
### CLIPS ###
#############
    def getClips(self, limit=50, offset=0):
        """ 
        limit: Number of items to return in a paged list.
        offset: Offset from start of a paged list.

        Get all Clips.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips
        """
        params = (
            ('limit', limit),
            ('offset', offset)
        )
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips', verify=False, headers=headers, params=params).json()
        return response

    def addClip(self, data):
        """ 
        Input: JSON Data

        Add a new clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips', verify=False, headers=headers, data=data).json()
        return response
    
    def addSubclip(self, clip_id, data):
        """ 
        Input: clip_id, JSON Data

        Add a Subclip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips__clip_id__subclip
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/subclip', verify=False, headers=headers, data=data).json()
        return response
    
    def getClipThumbnail(self, clip_id, frame=100, width=300, timecode='00:00:10:00'):
        """ 
        Input: clip_id

        Get a clip's thumbnail.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__thumbnail
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        params = (
            ('frame', frame),
            ('width', width),
            ('timecode', timecode)
        )
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/thumbnail', verify=False, headers=headers, params=params).json()
        return response
    
    def getClipUnc(self, clip_id):
        """ 
        Input: clip_id

        Get UNC paths for the given clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__unc
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/unc', verify=False, headers=headers).json()
        return response
    
    def updateClipData(self, clip_id, data):
        """ 
        Input: clip_id, Data in JSON format

        Update various clip details.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/put_clips__clip_id_
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/clips/'+clip_id, verify=False, headers=headers, json=data).json()
        return response

    def getClipData(self, clip_id, markers=False, proxy_details=False, display=True, custom_types=True, asset_site=True, checkexists=False, marker_comments=False, include_associations=False, include_descriptors=False):
        """ 
        Input: clip_id

        Get details about clip with specified id.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id_
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        params = (
            ('markers', markers),
            ('proxy_details', proxy_details),
            ('display', display),
            ('custom_types', custom_types),
            ('asset_site', asset_site),
            ('checkexists', checkexists),
            ('marker_comments', marker_comments),
            ('inculde_associations', include_associations),
            ('include_descriptors', include_descriptors)
        )
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id, verify=False, headers=headers, params=params).json()
        def keyExists(key):
            var = response.get(key)
            if var:
                var = response[key]
            else:
                var = None 
            return var
        class ClipData:
            def __init__(
                self, response, aaf_filename, aaf_path, asset, audio, capture, clip_id, display_aspect_ratio, display_audio, 
                display_filesize, display_filetype, display_frame_rate, display_name, display_standard, display_video_codec, 
                display_video_size, has_audio, has_data, has_index_file, has_video, is_recording, metadata, mob_ids, proxy_filename,
                proxy_has_index_file, proxy_id, proxy_path, status_flags, status_text, video
                ):
                self.data = response
                self.aaf_filename = aaf_filename
                self.aaf_path = aaf_path
                self.asset = asset
                self.audio = audio
                self.capture = capture
                self.clip_id = clip_id
                self.display_aspect_ratio = display_aspect_ratio
                self.display_audio = display_audio
                self.display_filesize = display_filesize
                self.display_filetype = display_filetype
                self.display_frame_rate = display_frame_rate
                self.display_name = display_name
                self.display_standard = display_standard
                self.display_video_codec = display_video_codec
                self.display_video_size = display_video_size
                self.has_audio = has_audio
                self.has_data = has_data
                self.has_index_file = has_index_file
                self.has_video = has_video
                self.is_recording = is_recording
                self.metadata = metadata
                self.mob_ids = mob_ids
                self.proxy_filename = proxy_filename
                self.proxy_has_index_file = proxy_has_index_file
                self.proxy_id = proxy_id
                self.proxy_path = proxy_path
                self.status_flags = status_flags
                self.status_text = status_text
                self.video = video
        #audio = keyExists("audio")
        clipdata = ClipData(
            response, keyExists('aaf_filename'), keyExists('aaf_path'), keyExists('asset'), keyExists("audio"),
            keyExists('capture'), keyExists('clip_id'), keyExists('display_aspect_ratio'), keyExists('display_audio'),
            keyExists('display_filesize'), keyExists('display_filetype'), keyExists('display_frame_rate'), keyExists('display_name'),
            keyExists('display_standard'), keyExists('display_video_codec'), keyExists('display_video_size'), keyExists('has_audio'),
            keyExists('has_data'), keyExists('has_index_file'), keyExists('has_video'), keyExists('is_recording'), keyExists('metadata'),
            keyExists('mob_ids'), keyExists('proxy_filename'), keyExists('proxy_has_index_file'), keyExists('proxy_id'), keyExists('proxy_path'),
            keyExists('status_flags'), keyExists('status_text'), keyExists('video')
            )
        return clipdata

    def deleteClip(self, clip_id):
        """ 
        Input: clip_id

        Delete a Clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/delete_clips__clip_id_
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/clips/'+clip_id, verify=False, headers=headers).json()
        return response

    def getFileDetails(self, clip_id):
        """ 
        Input: clip_id

        Get file ids that make up a clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__file_details
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/file_details', verify=False, headers=headers).json()
        return response

    def getFileIds(self, clip_id):
        """ 
        Input: clip_id

        Get file ids that make up a clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__file_ids
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/file_ids', verify=False, headers=headers).json()
        return response

    def getClipLocation(self, clip_id):
        """ 
        Input: clip_id

        Get CLip locations.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__locations
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/locations', verify=False, headers=headers).json()
        return response

    def addProxyLink(self, clip_id, data):
        """ 
        Input: "clip_id", JSON Data

        Add information about in which media space its proxy file has been made available.
        Payload only requires media space name or media space uuid, not necessarily both.
        The proxy filename is the name we want to give to the proxy when made available in the media space.
        NOTE - this call does not perform the copy or create the symlink, but only tells the database that such access to the proxy file now is available.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips__clip_id__proxy_links
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/proxy_links', verify=False, headers=headers, data=data).json()
        return response

    def deleteProxyLink(self, clip_id):
        """ 
        Input: "clip_id"

        Delete Proxy links.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/delete_clips__clip_id__proxy_links
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/proxy_links', verify=False, headers=headers).json()
        return response

    def getProxyLink(self, clip_id):
        """ 
        Input: "clip_id"

        Get Proxy links.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__proxy_links
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/proxy_links', verify=False, headers=headers).json()
        return response

    def updateImageSequence(self, clip_id, data):
        """ 
        Input: clip_id, JSON Data

        For clips that represent images sequences this allows you to append files.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/put_clips__clip_id__image_sequence
        """
        if type(clip_id) == int:
            clip_id = str(clip_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/clips/'+clip_id+'/image_sequence', verify=False, headers=headers, data=data).json()
        return response

    def addPlaceholder(self, data):
        """ 
        Input: JSON Data

        Add a new placeholder

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips_placeholders
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/clips/placeholders', verify=False, headers=headers, json=data).json()
        return response
    
    def addClipsToIngest(self, data):
        """ 
        Input: JSON Data

        Notify clips that are being captured by an ingest server.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/put_clips_status
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/clips/status', verify=False, headers=headers, data=data).json()
        return response

################      
### METADATA ###
################
    def updateMetadata(self, metadata_id, data):
        if type(metadata_id) == int:
            metadata_id = str(metadata_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/metadata/'+metadata_id, verify=False, headers=headers, json=data).json()
        return response

#######################        
### CUSTOM METADATA ###
#######################
    def getCustomMetadataConfig(self):
        """ 
        Get Custom Metadata configurations available to a user.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/get_custom_metadata_configurations
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_metadata_configurations', verify=False, headers=headers).json()
        return response

    def addCustomMetadataConfig(self, data):
        """ 
        Input: JSON Data

        Add a new Custom Meta Data Configuration. (Admin users olny)

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/post_custom_metadata_configurations
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/custom_metadata_configurations', verify=False, headers=headers, data=data).json()
        return response

    def deleteCustomMetadataConfig(self, configuration_id):
        """ 
        Input: configuration_id

        Delete a Custom Metadata Configuration.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/delete_custom_metadata_configurations__configuration_id_
        """
        if type(configuration_id) == int:
            configuration_id = configuration_id
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/custom_metadata_configurations/'+configuration_id, verify=False, headers=headers).json()
        return response
    
    def updateCustomMetadataConfig(self, configuration_id, data):
        """ 
        Input: configuration_id, JSON Data

        Update a Custom Metadata Configuration.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/put_custom_metadata_configurations__configuration_id_
        """
        if type(configuration_id) == int:
            configuration_id = configuration_id
        response = self.session.put('https://'+self.server+':8006/api/v2/database/custom_metadata_configurations/'+configuration_id, verify=False, headers=headers, data=data).json()
        return response

    def getBasicCustomMetadataConfig(self):
        """ 
        Get a basic list of a user's Custom Metadata Configurations.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/get_custom_metadata_configurations_basic_true
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_metadata_configurations?basic=true', verify=False, headers=headers).json()
        return response

    def getCustomMetadataFields(self):
        """ 
        Get all custom meta data fields.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_fields
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_metadata_fields', verify=False, headers=headers).json()
        return response

    def addCustomMetadataField(self, data):
        """ 
        Input: JSON Data

        Add a new custom metadata field.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/post_custom_metadata_fields
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/custom_metadata_fields', verify=False, headers=headers, data=data).json()
        return response

    def deleteCustomMetadataField(self, custom_field_id):
        """ 
        Input: custom_field_id

        Delete a custom metadata field.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/delete_custom_metadata_fields__custom_field_id_
        """
        if type(custom_field_id) == int:
            custom_field_id = str(custom_field_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/custom_metadata_fields/'+custom_field_id, verify=False, headers=headers).json()
        return response

    def getCustomMetadataField(self, custom_field_id):
        """ 
        Input: custom_field_id or custom_field_uuid
            custom_field_uuid has to be String

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_fields__custom_field_id_
        """
        if type(custom_field_id) == int:
            custom_field_id = str(custom_field_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_metadata_fields/'+custom_field_id, verify=False, headers=headers).json()
        return response

    def updateCustomMetadataFieldUI(self, custom_field_id, data):
        """ 
        Input: custom_field_id, JSON Data
        
        Update Custom Metadata Field's UI options.
            UI options are: normal, buttons, icons

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/put_custom_metadata_fields__custom_field_id_
        """
        if type(custom_field_id) == int:
            custom_field_id = str(custom_field_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/custom_metadata_fields/'+custom_field_id, verify=False, headers=headers, data=data).json()
        return response

    def getCustomMetadataGroupsUI(self):
        """ 
        Get custom metadata ui groups for configuration.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_groups
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_metadata_groups', verify=False, headers=headers).json()
        return response

    def getCustomMetadataGroupUI(self, custom_metadata_group_id):
        """ 
        Input: custom_metadata_group_id
        
        Get custom metadata ui group.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_groups__custom_metadata_group_id_
        """
        if type(custom_metadata_group_id) == int:
            custom_metadata_group_id = str(custom_metadata_group_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_metadata_fields/'+custom_metadata_group_id, verify=False, headers=headers).json()
        return response

    def getCustomMetadataTypes(self):
        """ 
        List all Custom Asset Types.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_asset_types', verify=False, headers=headers).json()
        return response

    def addCustomMetadataType(self, data):
        """ 
        Input: JSON Data
        
        Add custom asset type.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/post_custom_asset_types
        """
        response = self.session.post('https://'+self.server+':8006/api/v2/database/custom_asset_types', verify=False, headers=headers, data=data).json()
        return response

    def deleteCustomMetadataType(self, custom_asset_type_id):
        """ 
        Input: custom_asset_type_id
        
        Delete a Custom Asset type.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/post_custom_asset_types
        """
        if type(custom_asset_type_id) == int:
            custom_asset_type_id = str(custom_asset_type_id)
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/custom_asset_types/'+custom_asset_type_id, verify=False, headers=headers).json()
        return response

    def getCustomMetadataType(self, custom_asset_type_id):
        """ 
        Input: custom_asset_type_id
        
        Get a Custom Asset type.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types__custom_asset_type_id_
        """
        if type(custom_asset_type_id) == int:
            custom_asset_type_id = str(custom_asset_type_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/custom_asset_types/'+custom_asset_type_id, verify=False, headers=headers).json()
        return response

    def updateCustomMetadataType(self, custom_asset_type_id):
        """ 
        Input: custom_asset_type_id
        
        Get a Custom Asset type.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types__custom_asset_type_id_
        """
        if type(custom_asset_type_id) == int:
            custom_asset_type_id = str(custom_asset_type_id)
        response = self.session.put('https://'+self.server+':8006/api/v2/database/custom_asset_types/'+custom_asset_type_id, verify=False, headers=headers).json()
        return response

############        
### FILE ###
############     
    def getFiles(self, hash=None, media_space=None, path=None, user=None, filename=None, filesize=None):
        """ 
        Input: custom_asset_type_id
        
        Get a File.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Files/get_files
        """
        params = (
            ('hash', hash),
            ('media_space', media_space),
            ('path', path),
            ('user', user),
            ('filename', filename),
            ('filesize', filesize)
        )
        response = self.session.get('https://'+self.server+':8006/api/v2/database/files', verify=False, headers=headers, params=params).json()
        return response
    def getFile(self, file_id):
        """ 
        Input: custom_asset_type_id
        
        Get a Custom Asset type.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types__custom_asset_type_id_
        """
        if type(file_id) == int:
            file_id = str(file_id)
        response = self.session.get('https://'+self.server+':8006/api/v2/database/files/'+file_id, verify=False, headers=headers).json()
        return response

###############        
### MARKERS ###
###############
    def getMarkers(self, capture_id=None, uuid='',  log_entry_sources='', custom=True, include_comments=True):
        """
        You must specify either the capture id or uuid.
            You can optionally specify a list of source types to include.

        Get all markers for a capture.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/get_log_entries
        """
        params = (
            ('capture_id', capture_id),
            ('uuid', uuid),
            ('log_entry_source', log_entry_sources),
            ('custom', custom),
            ('include_comments', include_comments)
        )
        
        response = self.session.get('https://'+self.server+':8006/api/v2/database/log_entries', verify=False, headers=headers, params=params).json()
        return response
    
    def addCustomMarker(self, capture_id, in_time, out_time, fps, field_id, text, color='#00ff00'):
        """
        Input: int(capture_id), str(in_time), str(out_time), int(fps), int(field_id), str(text)
            Timcode format for in and out: HH:MM:SS:FF
            optional: color='hex'

        Get all markers for a capture.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/get_log_entries
        """
        data = {
            'capture_id': capture_id,
            'in_time': in_time+':'+str(fps)+'/1',
            'out_time': out_time+':'+str(fps)+'/1',
            'custom': {
                'field_'+str(field_id): text
            },
            'color': color
        }
        response = self.session.post('https://'+self.server+':8006/api/v2/database/log_entries', verify=False, headers=headers, json=data).json()
        return response

    def deleteCustomMarker(self, log_entry_id):
        """
        Input: log_entry_id

        Delete Marker.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/delete_log_entries__log_entry_id_
        """
        response = self.session.delete('https://'+self.server+':8006/api/v2/database/log_entries/'+str(log_entry_id), verify=False, headers=headers).json()
        return response
    
    def updateCustomMarker(self, log_entry_id, field_id, text, color='#00ff00'):
        """
        Input: int(capture_id), str(in_time), str(out_time), int(fps), int(field_id), str(text)

        Get all markers for a capture.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/get_log_entries
        """
        data = {
            'custom': {
                'field_'+str(field_id): text
            },
            'color': color
        }
        response = self.session.put('https://'+self.server+':8006/api/v2/database/log_entries/'+str(log_entry_id), verify=False, headers=headers, json=data).json()
        return response

##############        
### SEARCH ###
##############
    def searchQuick(self, term):
        """ 
        Input: Searchterm as String

        Returns Clip ids of search result
        """
        term = str(term)
        response = self.session.get('https://'+self.server+':8006/api/v2/search?q='+term, verify=False, headers=headers).json()
        clipids = []
        for hit in response:
            clipids.append(hit['clip_id'])
        return clipids

    def getMediaSpaceClips(self, mediaspace):
        """ 
        Input: Mediaspace Name

        Returns all Clip ids of the Mediaspace
        """
        mediaspace = str(mediaspace)
        response = self.session.get('https://'+self.server+':8006/api/v2/search?mediaspace='+mediaspace, verify=False, headers=headers).json()
        clipids = []
        for hit in response:
            if "clip_id" in hit:
                clipids.append(hit['clip_id'])
        return clipids

    def getMediaSpaces(self):
        """ 
        Returns all avialable Mediaspacesdata for User
        """
        response = self.session.get('https://'+self.server+':8006/api/v2/database/mediaspaces', verify=False, headers=headers).json()
        return response

    def searchAdvanced(self, data):
        """
        Advanced search.

        Data Example:
        {
            "combine": "MATCH_ALL",
            "filters": [
                    {
                        "field": {
                            "fixed_field": "CLIPNAME",
                            "group": "SEARCH_FILES",
                            "read_only": true,
                            "type": "QString"
                        },
                        "match": "BEGINS_WITH",
                        "search": "Rivers"
                    },
                    {
                        "field": {
                            "fixed_field": "MEDIA_SPACES_NAMES",
                            "group": "SEARCH_FILES",
                            "read_only": true,
                            "type": "QString"
                        },
                    "match": "EQUAL_TO",
                    "search": "LandscapesMediaSpace"
                    }
                ]
        }

        """
        response = self.session.post('https://'+self.server+':8006/api/v2/search', verify=False, json=data, headers=headers).json()
        return response

    



################################################### FLOW TRANSFER ################################################################

class FlowTransfer:
    """ 
    connect to EditShare Server:

    FlowTransfer("ip", "username", "password")

    FlowTransfer.connection returns <Response [200]> if connected
    """
    def __init__(self, ip, user, password) -> None:
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.server = ip
        user = user
        password = password
        self.session.auth = (user, password)
        data = [user, password]
        self.connection = self.session.post('https://'+self.server+':8006/api/v2/admin/check_password', verify=False, headers=headers, json=data)
        pass

############       
### COPY ###
############
    def getCopy(self):
        response = self.session.get('https://'+self.server+':8006/api/v2/transfer/copy', verify=False, headers=headers).json()
        return response

    def copyClipsById(self, source_file_id, destination_mediaspace):
        data = {"copy_operation_list": [
                {
                "destination_mediaspace": destination_mediaspace,
                "source_clip_id": source_file_id
                }
            ]
        }
        response = self.session.post('https://'+self.server+':8006/api/v2/transfer/copy', verify=False, headers=headers, json=data).json()
        return response


################################################### FLOW ADMIN ################################################################       

class FlowAdmin:
    """ 
    connect to EditShare Server:

    FlowAdmin("ip", "username", "password")

    FlowTransfer.connection returns <Response [200]> if connected
    """
    def __init__(self, ip, user, password) -> None:
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.server = ip
        user = user
        password = password
        self.session.auth = (user, password)
        data = [user, password]
        self.connection = self.session.post('https://'+self.server+':8006/api/v2/admin/check_password', verify=False, headers=headers, json=data)
        pass


 ################################################### STORAGE ################################################################       

class Storage:
    """ 
    connect to EditShare Server:

    FlowTransfer("ip", "username", "password")
        *only works with the "editshare" user

    FlowTransfer.connection returns <Response [200]> if connected
    """
    def __init__(self, ip, user, password) -> None:
        urllib3.disable_warnings()
        self.session = requests.Session()
        self.server = ip
        user = user
        password = password
        self.session.auth = (user, password)
        data = [user, password]
        self.connection = self.session.post('https://'+self.server+':8006/api/v1/storage/auth', verify=False, headers=headers)
        pass

    def getSpaces(self):
        """ 
        Returns all avialable Spaces for User
        """
        response = self.session.get('https://'+self.server+':8006/api/v1/storage/spaces?details=true', verify=False, headers=headers).json()    
        return response
