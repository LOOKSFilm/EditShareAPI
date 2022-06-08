# EditShareAPI
This is a Python module for the Editshare API: https://developers.editshare.com/


## Install on Windows
Copy EditShareAPI to `.\Users\$USER\AppData\Local\Programs\Python\Python310\Lib\site-pakages`

### Dependencies
```
pip install requests
```
```
pip install urllib3
```

### Import
```Python
import EditShareAPI
```

### Login
```Python
EditShareAPI.login("Server IP", "USER", "PASSWORD")
```


## Flow Metadata
https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata

### Import
```Python
From EditShareAPI import FlowMetadata
```

### get all Clip-Ids of a Mediaspace
```Python
FlowMetadata.getMediaSpaceClips("MediaSpaceName")
```
