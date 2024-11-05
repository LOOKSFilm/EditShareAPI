# EditShareAPI (WIP)
A Python module for the Editshare API: https://developers.editshare.com/


## Install
1. create Python Virtual Environment
```bash
python -m venv .venv
```
2. clone repo in .venv/Lib/site-packages
```bash
gh repo clone LOOKSFilm/EditShareAPI .\.venv\Lib\site-packages\EditShareAPI
```
3. install requests
```bash
pip install requests
```
or via requirements.txt
```bash
pip install -r .\.venv\Lib\site-packages\EditShareAPI\requirements.txt
```

### Import
Import different classes e.g.:
```Python
from EditShareAPI import EsAuth, FlowMetadata
```
Available Classes are: 
 - EsAuth
 - EsTransfer
 - EsMount
 - FlowMetadata
 - FlowAdmin
 - FlowAutomation
 - FlowSearch

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
