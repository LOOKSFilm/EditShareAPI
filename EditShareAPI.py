import requests
import urllib3
import json

class EsAuth:
    def login(ip, user, password) -> None:
            urllib3.disable_warnings()
            global session
            session = requests.Session()
            global server
            server = ip
            global dbUrl
            dbUrl = f"https://{server}:8006/api/v2/database"
            global searchUrl
            searchUrl = f"https://{server}:8006/api/v2/search"
            global automationUrl
            automationUrl = f"https://{server}:8006/api/v2/automation"
            global mountUrl
            mountUrl = f"https://{server}:8006/api/v2/mount"
            global scanUrl
            scanUrl = f"https://{server}:8006/api/v2/scan"
            session.auth = (user, password)
            #print(session.auth)
            data = [user, password]
            connection = session.post(f"https://{server}:8006/api/v2/admin/check_password", verify=False, json=data)
            return connection.status_code

class FlowMetadata:
#############
### ASSET ###
#############
    def ping():
        ping = session.get(f"{dbUrl}/ping", verify=False)
        return ping
    
    def addAsset(data):
        """ 
        Input: dict

        Adds an asset.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/post_assets
        """
        response = session.post(f"{dbUrl}/assets", verify=False, data=data)
        return response

    def getAsset(asset_id, vendor_data=False):
        """ 
        Input: asset_id or uuid

        Get AssetData Object. (.data for JSON)

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets__asset_id_
        """
        response = session.get(f"{dbUrl}/assets/{asset_id}", verify=False).json()
        return response
    
    def updateAsset(asset_id, data):
        """ 
        Input: asset_id or uuid

        Update asset Metadata.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/put_assets__asset_id_
        """
        response = session.put(f"{dbUrl}/assets/{asset_id}", verify=False, data=data)
        return response
    
    def deleteAsset(asset_id):
        """ 
        Input: asset_id or uuid

        Delete asset data entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/delete_assets__asset_id_
        """
        response = session.delete(f"{dbUrl}/assets/{asset_id}", verify=False)
        return response
    
    def getAssetVendorData(asset_id):
        """ 
        Input: asset_id

        Get vendor data associated with an asset.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets__asset_id__vendor_data
        """
        response = session.get(f"{dbUrl}/assets/{asset_id}/vendor_data", verify=False).json()
        return response
    
    def getAssetAssociations(asset_id):
        """ 
        Input: asset_id or asset_collection_id or uuid

        Get asset associations by id.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets__uuid__associations
        """
        response = session.get(f"{dbUrl}/assets/{asset_id}/associations", verify=False).json()
        return response

    def associateAsset(asset_id, associated_asset_id):
        """ 
        Input: asset_id, asset_association_id

        Associate another asset with "this" one.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/put_assets__asset_id__associations__associated_asset_id_
        """
        response = session.put(f"{dbUrl}/assets/{asset_id}/associations/{associated_asset_id}", verify=False).json()
        return response

    def deleteAssociation(asset_id, associated_asset_id):
        """ 
        Input: asset_id, asset_association_id

        Delete an asset association entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/delete_assets__asset_id__associations__associated_asset_id_
        """
        response = session.delete(f"{dbUrl}/assets/{asset_id}/associations/{associated_asset_id}", verify=False).json()
        return response

    def addAssetAssosiation(data):
        """ 
        Input: dict
        Add an asset association.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/post_assets_associations
        """
        response = session.post(f"{dbUrl}/assets/associations", verify=False, data=data).json()
        return response

    def getAssetAssosiation(asset_collection_id):
        """ 
        Input: asset_collection_id or uuid

        Get an asset association

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/get_assets_associations__asset_collection_id_
        """
        response = session.get(f"{dbUrl}/assets/associations/{asset_collection_id}", verify=False).json()
        return response
    def addAssetAssosiation(asset_collection_id):
        """ 
        Input: asset_collection_id or uuid

        Modify an asset association, using the association"s database ID.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/put_assets_associations__asset_collection_id_
        """
        response = session.put(f"{dbUrl}/assets/associations/{asset_collection_id}", verify=False).json()
        return response
    
    def deleteAssetAssosiation(asset_collection_id):
        """ 
        Input: asset_collection_id or uuid

        Delete an asset association, using the association"s database ID
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Assets%20and%20Asset%20Metadata/delete_assets_associations__asset_collection_id_
        """
        response = session.delete(f"{dbUrl}/assets/associations/{asset_collection_id}", verify=False).json()
        return response

    def exportMetadata(asset_id):
        """
        Input: asset_id

        Exports the Metadata of an Asset in XML format. (ver. 2022.2)
        """
        params = {
            "export_format": "xml",
            "asset_metadata": "true",
            "asset_custom_metadata": "true",
            "file_details": "true",
            "location_details": "true",
            "backup_details": "true",
            "markers": "true",
            "csv_framerates": "false",
            "csv_comments": "false",
            "csv_bom": "false",
        }
        response = session.get(f"{dbUrl}/assets/{asset_id}/export", params=params)
        return response

###############
### CAPTURE ###
###############
    def addCapture(data, createcaptureonly=False):
        """ 
        Input: dict

        Create new capture. If the cature id or recording id exists only a new chunk group is created.
        """
        params = (
            ("createcaptureonly", createcaptureonly)
        )
        response = session.post(f"{dbUrl}/captures", data=data, params=params)
        return response

    def deleteCapture(capture_id):
        """ 
        Input: capture_id or uuid

        Delete a capture entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/delete_captures__capture_id_
        """
        response = session.delete(f"{dbUrl}/captures/{capture_id}", verify=False)
        return response

    def getCapture(capture_id):
        """ 
        Input: capture_id

        Get details about capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id_
        """
        response = session.get(f"{dbUrl}/captures/{capture_id}", verify=False)
        return response

    def updateCapture(capture_id, data):
        """ 
        Input: capture_id, dict

        Update capture data.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/put_captures__capture_id_
        """
        response = session.put(f"{dbUrl}/captures/{capture_id}", verify=False, data=data)
        return response

    def getCaptureClips(capture_id):
        """ 
        Input: capture_id

        Get Clips in a capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id__clips
        """
        response = session.get(f"{dbUrl}/captures/{capture_id}/clips", verify=False)
        return response

    def getChunkGroup(capture_id):
        """ 
        Input: capture_id

        Get chunk groups in capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id__groups
        """
        response = session.get(f"{dbUrl}/captures/{capture_id}/groups", verify=False)
        return response

    def getChunkGroupClips(capture_id, chunk_group_id):
        """ 
        Input: capture_id, chunk_group_id

        Get the clips in the specified chunk group for a particular capture.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/get_captures__capture_id__groups__chunk_group_id_
        """
        response = session.get(f"{dbUrl}/captures/{capture_id}/groups/{chunk_group_id}", verify=False)
        return response

    def deleteCaptureLogEntries(capture_id, log_entry_sources="user,qc,ingest,import,audio_metadata,video_metadata,review_approve"):
        """ 
        Input: capture_id

        Delete all the log entries for a capture. You can specify a uuid or id, and limit to a type (or types) of log entry.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Captures/delete_captures__capture_id__log_entries
        """
        params = (
            ("log entry sources", log_entry_sources)
        )
        response = session.get(f"{dbUrl}/captures/{capture_id}/log_entries", verify=False, params=params)
        return response

#############
### CLIPS ###
#############
    def getClips(limit=50, offset=0):
        """ 
        limit: Number of items to return in a paged list.
        offset: Offset from start of a paged list.

        Get all Clips.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips
        """
        params = (
            ("limit", limit),
            ("offset", offset)
        )
        response = session.get(f"{dbUrl}/clips", verify=False, params=params).json()
        return response

    def addClip(data):
        """ 
        Input: dict

        Add a new clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips
        """
        response = session.get(f"{dbUrl}/clips", verify=False, data=data).json()
        return response
    
    def addSubclip(clip_id, data):
        """ 
        Input: clip_id, dict

        Add a Subclip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips__clip_id__subclip
        """
        response = session.get(f"{dbUrl}/clips/{clip_id}/subclip", verify=False, data=data).json()
        return response
    
    def getClipThumbnail(clip_id, frame=100, width=300, timecode="00:00:10:00"):
        """ 
        Input: clip_id ; optinal: frame, width, timecode ("hh:mm:ss:ff")

        Get a clip"s thumbnail.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__thumbnail
        """
        params = (
            ("frame", frame),
            ("width", width),
            ("timecode", timecode)
        )
        response = session.get(f"{dbUrl}/clips/{clip_id}/thumbnail", verify=False, params=params).json()
        return response
    
    def getClipUnc(clip_id):
        """ 
        Input: clip_id

        Get UNC paths for the given clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__unc
        """
        response = session.get(f"{dbUrl}/clips/{clip_id}/unc", verify=False).json()
        return response
    
    def updateClipData(clip_id, data):
        """ 
        Input: clip_id, dict

        Update various clip details.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/put_clips__clip_id_
        """
        response = session.put(f"{dbUrl}/clips/{clip_id}", verify=False, data=data).json()
        return response

    def getClipData(clip_id, markers=False, proxy_details=False, display=True, custom_types=True, asset_site=True, checkexists=False, marker_comments=False, include_associations=False, include_descriptors=False):
        """ 
        Input: clip_id

        returns object-like data of a Clips metadata

        Get details about clip with specified id.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id_
        """
    
        params = (
            ("markers", markers),
            ("proxy_details", proxy_details),
            ("display", display),
            ("custom_types", custom_types),
            ("asset_site", asset_site),
            ("checkexists", checkexists),
            ("marker_comments", marker_comments),
            ("inculde_associations", include_associations),
            ("include_descriptors", include_descriptors)
        )
        response = session.get(f"{dbUrl}/clips/{clip_id}", verify=False, params=params).json()
        return response

    def deleteClip(clip_id):
        """ 
        Input: clip_id

        Delete a Clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/delete_clips__clip_id_
        """
        response = session.delete(f"{dbUrl}/clips/{clip_id}", verify=False).json()
        return response

    def getFileDetails(clip_id):
        """ 
        Input: clip_id

        Get file ids that make up a clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__file_details
        """
        response = session.get(f"{dbUrl}/clips/{clip_id}/file_details", verify=False).json()
        return response

    def getFileIds(clip_id):
        """ 
        Input: clip_id

        Get file ids that make up a clip.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__file_ids
        """
        response = session.get(f"{dbUrl}/clips/{clip_id}/file_ids", verify=False).json()
        return response

    def getClipLocation(clip_id):
        """ 
        Input: clip_id

        Get CLip locations.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__locations
        """
        response = session.get(f"{dbUrl}/clips/{clip_id}/locations", verify=False).json()
        return response

    def addProxyLink(clip_id, data):
        """ 
        Input: "clip_id", JSON Data

        Add information about in which media space its proxy file has been made available.
        Payload only requires media space name or media space uuid, not necessarily both.
        The proxy filename is the name we want to give to the proxy when made available in the media space.
        NOTE - this call does not perform the copy or create the symlink, but only tells the database that such access to the proxy file now is available.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips__clip_id__proxy_links
        """
        response = session.post(f"{dbUrl}/clips/{clip_id}/proxy_links", verify=False, data=data).json()
        return response

    def deleteProxyLink(clip_id):
        """ 
        Input: "clip_id"

        Delete Proxy links.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/delete_clips__clip_id__proxy_links
        """
        response = session.delete(f"{dbUrl}/clips/{clip_id}/proxy_links", verify=False).json()
        return response

    def getProxyLink(clip_id):
        """ 
        Input: "clip_id"

        Get Proxy links.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/get_clips__clip_id__proxy_links
        """
        response = session.get(f"{dbUrl}/clips/{clip_id}/proxy_links", verify=False).json()
        return response

    def updateImageSequence(clip_id, data):
        """ 
        Input: clip_id, JSON Data

        For clips that represent images sequences this allows you to append files.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/put_clips__clip_id__image_sequence
        """
        response = session.put(f"{dbUrl}/clips/{clip_id}/image_sequence", verify=False, data=data).json()
        return response

    def addPlaceholder(data):
        """ 
        Input: JSON Data

        Add a new placeholder

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/post_clips_placeholders
        """
        response = session.post(f"{dbUrl}/clips/placeholders", verify=False, data=data).json()
        return response
    
    def addClipsToIngest(data):
        """ 
        Input: JSON Data

        Notify clips that are being captured by an ingest server.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Clips/put_clips_status
        """
        response = session.post(f"{dbUrl}/clips/status", verify=False, data=data).json()
        return response

################      
### METADATA ###
################
    def updateMetadata(metadata_id, data):
        response = session.put(f"{dbUrl}/metadata/{metadata_id}", verify=False, data=data).json()
        return response

#######################        
### CUSTOM METADATA ###
#######################
    def getCustomMetadataConfig():
        """ 
        Get Custom Metadata configurations available to a user.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/get_custom_metadata_configurations
        """
        response = session.get(f"{dbUrl}/custom_metadata_configurations", verify=False).json()
        return response

    def addCustomMetadataConfig(data):
        """ 
        Input: JSON Data

        Add a new Custom Meta Data Configuration. (Admin users olny)

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/post_custom_metadata_configurations
        """
        response = session.post(f"{dbUrl}/custom_metadata_configurations", verify=False, data=data).json()
        return response

    def deleteCustomMetadataConfig(configuration_id):
        """ 
        Input: configuration_id

        Delete a Custom Metadata Configuration.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/delete_custom_metadata_configurations__configuration_id_
        """
        response = session.delete(f"{dbUrl}/custom_metadata_configurations/{configuration_id}", verify=False).json()
        return response
    
    def updateCustomMetadataConfig(configuration_id, data):
        """ 
        Input: configuration_id, JSON Data

        Update a Custom Metadata Configuration.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/put_custom_metadata_configurations__configuration_id_
        """
        response = session.put(f"{dbUrl}/custom_metadata_configurations/{configuration_id}", verify=False, data=data).json()
        return response

    def getBasicCustomMetadataConfig():
        """ 
        Get a basic list of a user"s Custom Metadata Configurations.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Metadata%20Configurations/get_custom_metadata_configurations_basic_true
        """
        response = session.get(f"{dbUrl}/custom_metadata_configurations?basic=true", verify=False).json()
        return response

    def getCustomMetadataFields():
        """ 
        Get all custom meta data fields.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_fields
        """
        response = session.get(f"{dbUrl}/custom_metadata_fields", verify=False).json()
        class Fields:
            def __init__(self, response):
                self.fields_dict = dict()  
                self.fields_data = response      
                for field in response:
                    self.fields_dict[field["name"]] = field["db_key"]
                self.fields_dict = {key: self.fields_dict[key] for key in sorted(self.fields_dict.keys())}
        fields = Fields(response)
        return fields
    
    def addCustomMetadataField(data):
        """ 
        Input: JSON Data

        Add a new custom metadata field.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/post_custom_metadata_fields
        """
        response = session.post(f"{dbUrl}/custom_metadata_fields", verify=False, data=data).json()
        return response

    def deleteCustomMetadataField(custom_field_id):
        """ 
        Input: custom_field_id

        Delete a custom metadata field.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/delete_custom_metadata_fields__custom_field_id_
        """
        response = session.delete(f"{dbUrl}/custom_metadata_fields/{custom_field_id}", verify=False).json()
        return response

    def getCustomMetadataField(custom_field_id):
        """ 
        Input: custom_field_id or custom_field_uuid
            custom_field_uuid has to be String

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_fields__custom_field_id_
        """
        params = {'db_key': custom_field_id}
        response = session.get(f"{dbUrl}/custom_metadata_fields/", params=params, verify=False).json()
        return response

    def updateCustomMetadataFieldUI(custom_field_id, data):
        """ 
        Input: custom_field_id, JSON Data
        
        Update Custom Metadata Field"s UI options.
            UI options are: normal, buttons, icons

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/put_custom_metadata_fields__custom_field_id_
        """
        response = session.put(f"{dbUrl}/custom_metadata_fields/{custom_field_id}", verify=False, data=data).json()
        return response

    def getCustomMetadataGroupsUI():
        """ 
        Get custom metadata ui groups for configuration.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_groups
        """
        response = session.get(f"{dbUrl}/custom_metadata_groups", verify=False).json()
        return response

    def getCustomMetadataGroupUI(custom_metadata_group_id):
        """ 
        Input: custom_metadata_group_id
        
        Get custom metadata ui group.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Metadata%20Fields/get_custom_metadata_groups__custom_metadata_group_id_
        """
        response = session.get(f"{dbUrl}/custom_metadata_fields/{custom_metadata_group_id}", verify=False).json()
        return response

    def getCustomMetadataTypes():
        """ 
        List all Custom Asset Types.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types
        """
        response = session.get(f"{dbUrl}/custom_asset_types", verify=False).json()
        return response

    def addCustomMetadataType(data):
        """ 
        Input: JSON Data
        
        Add custom asset type.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/post_custom_asset_types
        """
        response = session.post(f"{dbUrl}/custom_asset_types", verify=False, data=data).json()
        return response

    def deleteCustomMetadataType(custom_asset_type_id):
        """ 
        Input: custom_asset_type_id
        
        Delete a Custom Asset type.

        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/post_custom_asset_types
        """
        response = session.delete(f"{dbUrl}/custom_asset_types/{custom_asset_type_id}", verify=False).json()
        return response

    def getCustomMetadataType(custom_asset_type_id):
        """ 
        Input: custom_asset_type_id
        
        Get a Custom Asset type.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types__custom_asset_type_id_
        """
        response = session.get(f"{dbUrl}/custom_asset_types/{custom_asset_type_id}", verify=False).json()
        return response

    def updateCustomMetadataType(custom_asset_type_id):
        """ 
        Input: custom_asset_type_id
        
        Get a Custom Asset type.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types__custom_asset_type_id_
        """
        response = session.put(f"{dbUrl}/custom_asset_types/{custom_asset_type_id}", verify=False).json()
        return response

############        
### FILE ###
############     
    def getFiles(hash=None, media_space=None, path=None, user=None, filename=None, filesize=None):
        """ 
        Input: custom_asset_type_id
        
        Get a File.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Files/get_files
        """
        params = (
            ("hash", hash),
            ("media_space", media_space),
            ("path", path),
            ("user", user),
            ("filename", filename),
            ("filesize", filesize)
        )
        response = session.get(f"{dbUrl}/files", verify=False, params=params).json()
        return response
    
    def getFile(file_id):
        """ 
        Input: custom_asset_type_id
        
        Get a Custom Asset type.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Custom%20Asset%20Types/get_custom_asset_types__custom_asset_type_id_
        """
        response = session.get(f"{dbUrl}/files/{file_id}", verify=False).json()
        return response

##############        
### IMAGES ###
##############
    def getImageData(image_id):
        response = session.get(f"{dbUrl}/images/{image_id}", verify=False).json()
        return response

    def updateImageData(image_id, data):
        response = session.put(f"{dbUrl}/images/{image_id}", data=data, verify=False).json()
        return response
    
###############        
### MARKERS ###
###############
    def getMarkers(capture_id=None, uuid="",  log_entry_sources="", custom=True, include_comments=True):
        """
        You must specify either the capture id or uuid.
            You can optionally specify a list of source types to include.

        Get all markers for a capture.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/get_log_entries
        """
        params = (
            ("capture_id", capture_id),
            ("uuid", uuid),
            ("log_entry_source", log_entry_sources),
            ("custom", custom),
            ("include_comments", include_comments)
        )
        
        response = session.get(f"{dbUrl}/log_entries", verify=False, params=params).json()
        return response
    
    def addCustomMarker(capture_id, in_time, out_time, fps, text, color="#00ff00"):
        """
        Input: int(capture_id), str(in_time), str(out_time), int(fps), int(field_id), str(text)
            Timcode format for in and out: HH:MM:SS:FF
            optional: color="hex"

        Get all markers for a capture.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/get_log_entries
        """
        data = dict()
        data["capture_id"] = capture_id
        data["in_time"] = f"{in_time}:{fps}/1"
        data["out_time"] = f"{out_time}:{fps}/1"
        data["comment"] = text
        # data["custom"] = dict()
        # data["custom"][field_id] = text
        data["color"] = color
        data = json.dumps(data)
        response = session.post(f"{dbUrl}/log_entries", verify=False, data=data).json()
        return response

    def deleteCustomMarker(log_entry_id):
        """
        Input: log_entry_id

        Delete Marker.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/delete_log_entries__log_entry_id_
        """
        response = session.delete(f"{dbUrl}/log_entries/{log_entry_id}", verify=False).json()
        return response
    
    def updateCustomMarker(log_entry_id, field_id, text, color="#00ff00"):
        """
        Input: int(capture_id), str(in_time), str(out_time), int(fps), int(field_id), str(text)

        Get all markers for a capture.
        
        https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata#/Markers/get_log_entries
        """
        data = dict()
        data["custom"] = dict()
        data["custom"][f"field_{field_id}"] = text
        data["color"] = color
        response = session.put(f"{dbUrl}/log_entries/{log_entry_id}", verify=False, data=data).json()
        return response

##############        
### SEARCH ###
##############
    def searchQuick(term):
        """ 
        Input: Searchterm as String

        Returns json of search result
        """
        response = session.get(f"{searchUrl}?q={term}", verify=False).json()
        results = []
        for hit in response:
            results.append(hit)
        return results

    def searchAdvanced(data):
        """
        Advanced search.

        """
        response = session.post(f"{searchUrl}/search", verify=False, data=data).json()
        return response

    def searchList(template=""):
        """
        Get a list fields that can be searched.

        """
        response = session.get(f"{searchUrl}/fields?template={template}", verify=False).json()
        return response
    
    def getMediaSpaceClips(mediaspace):
        """ 
        Input: Mediaspace Name

        Returns all Clip ids of the Mediaspace
        """
        response = session.get(f"{searchUrl}?mediaspace={mediaspace}", verify=False).json()
        return response

    def getMediaSpaces():
        """ 
        Returns all avialable Mediaspacesdata for User
        """
        response = session.get(f"{dbUrl}/mediaspaces/all", verify=False).json()
        return response
    
    def deleteMediaSpace(mediaspace_id, from_database=False):
        """ 
        Returns all avialable Mediaspacesdata for User
        """
        params = dict()
        params["from_database"] = from_database
        response = session.delete(f"{dbUrl}/mediaspaces/{mediaspace_id}", params=params, verify=False).json()
        return response
    
############       
### Scan ###
############
class Scan:
    def getScanJobs():
        """
        Get a list of Scan Jobs
        """
        response = session.get(f"{scanUrl}/jobs").json()
        return response
    
    def stopScanJob(uuid):
        """
        Stop a Scan Job
        """
        response = session.put(f"{scanUrl}/jobs/{uuid}/stop").json()
        return response
    
    def scanAsset(data):
        """
        scan an Asset
        """
        response = session.post(f"{scanUrl}/asset", data=data).json()
        return response
    
    def getAssetScanState(scan_job_uuid):
        """
        returns the state of an Asset scan job
        """
        response = session.get(f"{scanUrl}/asset/{scan_job_uuid}").json()
        return response
##################       
### Automation ###
##################
class FlowAutomation:
    def getAutomationJobs():
        """
        Get a list of Automation Jobs
        """
        response = session.get(f"{automationUrl}/jobs").json()
        return response
    
    def deleteAutomationJob(uuid):
        """
        Delete a Automation Job
        """
        response = session.delete(f"{automationUrl}/jobs/{uuid}").json()
        return response
    def getTemplates():
        """
        get a list of templates
        """
        response = session.get(f"{automationUrl}/templates").json()
        return response
    def loadTemplate(data):
        """
        Load Template from JSON
        """
        response = session.post(f"{automationUrl}/templates/load", data=data).json()
        return response
    def deactivateTemplate(uuid):
        """
        deactivate a Template
        """
        response = session.put(f"{automationUrl}/templates/{uuid}/deactivate").json()
        return response
    def activateTemplate(uuid):
        """
        activate a Template
        """
        response = session.put(f"{automationUrl}/templates/{uuid}/activate").json()
        return response
    def updateTemplate(uuid, data):
        """
        Update a Template
        """
        params = {"validate": "true"}
        response = session.put(f"{automationUrl}/templates/{uuid}", data=data, params=params).json()
        return response
    def triggerExternalTemplate(uuid, data):
        """
        Trigger an External Template
        """
        response = session.put(f"{automationUrl}/templates/external/{uuid}/trigger", data=data).json()
        return response
    def getJob(uuid):
        """
        Get an automation job status
        """
        """
        Trigger an External Template
        """
        response = session.get(f"{automationUrl}/jobs/{uuid}").json()
        return response
    def getJobStatus(uuid):
        """
        Get an automation job status
        """
        """
        Trigger an External Template
        """
        response = session.get(f"{automationUrl}/jobs/{uuid}/status").json()
        return response
    def getJobTasks(uuid):
        """
        Get an automation job status
        """
        """
        Trigger an External Template
        """
        response = session.get(f"{automationUrl}/jobs/{uuid}/tasks").json()
        return response


#############      
### Mount ###
#############
class EsMount:
    def mount(directory, data):
        data = data
        data["default_directory"]["directory"] = directory
        print(json.dumps(data, indent=4))
        data = json.dumps(data)
        response = session.put(f"{mountUrl}/mount", data=data)
        return response
