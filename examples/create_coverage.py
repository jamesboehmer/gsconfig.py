#def createPageCoverage(catalog, workspace, name, fileURL, xPixelOffset, pixelWidth, pixelHeight):    
from geoserver.catalog import Catalog
from geoserver.workspace import Workspace
from geoserver.resource import UnsavedCoverage

cartesianEPSG='EPSG:404000'
webMercatorEPSG='EPSG:3857'

workspaceName='TestWorkspace'
coverageStoreName='TestCoverageStore'
coverageFileURL='relative/path/to/some/file.tiff'
coverageName='TestCoverage'
coverageEnabled=False

catalog = Catalog("http://localhost:8080/geoserver/rest","admin", "geoserver")
workspace = Workspace(catalog, workspaceName)

#Set up the coverage store using the tiff
unsavedCoverageStore = UnsavedCoverageStore(catalog, coverageStoreName, workspace)
unsavedCoverageStore.dirty['url']='file:%s' % coverageFileURL
unsavedCoverageStore.dirty['enabled']='true'
unsavedCoverageStore.dirty['configure']='all'
catalog.save(unsavedCoverageStore)

coverageStore = CoverageStore(catalog, workspace, coverageStoreName)

unsavedCoverage = UnsavedCoverage(catalog, workspace, coverageStore, coverageName)
unsavedCoverage.name=coverageName;
unsavedCoverage.title='Coverage Title';
unsavedCoverage.abstract='Coverage Abstract'
unsavedCoverage.enabled=coverageEnabled

unsavedCoverage.dirty['name']=coverage.name
unsavedCoverage.dirty['title']=coverage.title
unsavedCoverage.dirty['abstract']=coverage.abstract
unsavedCoverage.dirty['description']='Coverage Description'
unsavedCoverage.dirty['nativeBoundingBox']=('West', 'East','South', 'North', cartesianEPSG)

unsavedCoverage.dirty['srs']=webMercatorEPSG
unsavedCoverage.dirty['projection_policy']='FORCE_DECLARED' #REPROJECT_TO_NATIVE
unsavedCoverage.dirty['keywords']=('WCS','GeoTIFF',coverageName)
unsavedCoverage.dirty['requestSRS']={cartesianEPSG}
unsavedCoverage.dirty['responseSRS']={cartesianEPSG}
unsavedCoverage.dirty['supportedFormats']=("GEOTIFF","GIF","PNG","JPEG","TIFF","ArcGrid","ImageMosaic","Gtopo30")
unsavedCoverage.dirty['interpolationMethods']=("nearest neighbor","bilinear","bicubic")
unsavedCoverage.dirty['defaultInterpolationMethod']="nearest neighbor"
unsavedCoverage.dirty['dimensions']=[CoverageDimension("PALETTE_INDEX", "GridSampleDimension",("-Infinity","Infinity"))]
unsavedCoverage.dirty['parameters']={'InputTransparentColor':'', 'SUGGESTED_TILE_SIZE':'512,512'}
unsavedCoverage.dirty['nativeFormat']='GeoTIFF'

print coverage.message()
catalog.save(unsavedCoverage)

#Geoserver will not honor enabedl=false when creating a coverage or featuretype, so set it after
if not coverageEnabled:
    layer = catalog.get_layer(coverageName)
    layer.enabled=False
    catalog.save(layer)
