# EditShareAPI
A Python module for the Editshare API: https://developers.editshare.com/


## Install ![](https://cdn.icon-icons.com/icons2/1488/PNG/32/5314-windows_102509.png)
Copy EditShareAPI to `.\Users\$USER\AppData\Local\Programs\Python\Python$version\Lib\site-pakages`

### Dependencies
```
pip install requests
```
```
pip install urllib3
```

### Login
```Python
from EditShareAPI import EsAuth
EsAuth.login("IP", "USER", "PASSWORD")
```
returns 200 if logged in


## Flow Metadata
https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata

### Import
```Python
from EditShareAPI import FlowMetadata
```

### get all Clip-Ids of a Mediaspace
```Python
FlowMetadata.getMediaSpaceClips("MediaSpaceName")
```
returns list of Clipids of the Mediaspace.
