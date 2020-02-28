import bpy
import gaffer_assetexchange.assetexchange_shared as assetexchange_shared
import gaffer_assetexchange.assetexchange_blender as assetexchange_blender
from . import functions


def import_hdri(asset, selectedVariants):
    # extract file paths and thumbnail path
    file_paths = []
    thumb_path = None

    # collect selected variants
    variantLabels, variantConfigs = assetexchange_shared.asset.explode_variants('Primary', selectedVariants)
    for variantConfig in variantConfigs:
        object_list = assetexchange_shared.asset.filter_objects_by_variant_config(asset, 'Primary', variantLabels, variantConfig)
        for obj in object_list:
            file_paths.append(obj["file"]["path"])

    # search for thumbnail
    samples = asset['assemblies'].get('Previews Gallery Samples', None)
    if samples is not None:
        sample_projection = samples['objects'].get('projection', None)
        if sample_projection is not None:
            thumb_path = sample_projection["file"]["path"]

    # add external hdris
    if len(file_paths) > 0:
        functions.add_external_hdri(bpy.context, asset['uid'], file_paths, thumb_path)


class AssetPushService(assetexchange_shared.server.AssetPushServiceInterface):
    # lists all supported asset types which can be pushed here
    def SupportedTypes(self, _):
        return [
            'environment.hdri',
        ]

    # checks if specific asset can be pushed here
    def PushAllowed(self, asset):
        return True

    # asset gets pushed here
    @assetexchange_blender.execute_on_main_thread
    def Push(self, data):
        if data['asset']['typeUid'] == 'environment.hdri':
            import_hdri(data['asset'], data['selectedVariants'])
            return True
        return False
