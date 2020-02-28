# Generated file

import sys, importlib.util

sys.modules["gaffer_assetexchange"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange", loader=None, is_package='True'))
sys.modules["gaffer_assetexchange.assetexchange_shared.common.environment"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.common.environment", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.common"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.common", loader=None, is_package=True))
sys.modules["gaffer_assetexchange.assetexchange_shared.asset.variants"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.asset.variants", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.asset"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.asset", loader=None, is_package=True))
sys.modules["gaffer_assetexchange.assetexchange_shared.server.services"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.server.services", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.server.registry"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.server.registry", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.server.protocol"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.server.protocol", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.server"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.server", loader=None, is_package=True))
sys.modules["gaffer_assetexchange.assetexchange_shared.client.registry"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.client.registry", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.client.basic"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.client.basic", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_shared.client"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared.client", loader=None, is_package=True))
sys.modules["gaffer_assetexchange.assetexchange_shared"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_shared", loader=None, is_package=True))
sys.modules["gaffer_assetexchange.assetexchange_blender.mainthread"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_blender.mainthread", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_blender.addon"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_blender.addon", loader=None, is_package=None))
sys.modules["gaffer_assetexchange.assetexchange_blender"] = importlib.util.module_from_spec(importlib.util.spec_from_loader("gaffer_assetexchange.assetexchange_blender", loader=None, is_package=True))


setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.common"], "environment", sys.modules["gaffer_assetexchange.assetexchange_shared.common.environment"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared"], "common", sys.modules["gaffer_assetexchange.assetexchange_shared.common"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.asset"], "variants", sys.modules["gaffer_assetexchange.assetexchange_shared.asset.variants"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared"], "asset", sys.modules["gaffer_assetexchange.assetexchange_shared.asset"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.server"], "services", sys.modules["gaffer_assetexchange.assetexchange_shared.server.services"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.server"], "registry", sys.modules["gaffer_assetexchange.assetexchange_shared.server.registry"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.server"], "protocol", sys.modules["gaffer_assetexchange.assetexchange_shared.server.protocol"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared"], "server", sys.modules["gaffer_assetexchange.assetexchange_shared.server"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.client"], "registry", sys.modules["gaffer_assetexchange.assetexchange_shared.client.registry"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared.client"], "basic", sys.modules["gaffer_assetexchange.assetexchange_shared.client.basic"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_shared"], "client", sys.modules["gaffer_assetexchange.assetexchange_shared.client"])
setattr(sys.modules["gaffer_assetexchange"], "assetexchange_shared", sys.modules["gaffer_assetexchange.assetexchange_shared"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_blender"], "mainthread", sys.modules["gaffer_assetexchange.assetexchange_blender.mainthread"])
setattr(sys.modules["gaffer_assetexchange.assetexchange_blender"], "addon", sys.modules["gaffer_assetexchange.assetexchange_blender.addon"])
setattr(sys.modules["gaffer_assetexchange"], "assetexchange_blender", sys.modules["gaffer_assetexchange.assetexchange_blender"])



exec('''import os
import errno


def environment_name():
    return os.getenv(\'ASSETNINJA_ENVIRONMENT\', \'primary\')


def runtime_path(*parts):
    path = os.path.expanduser("~")
    # workaround required for 2.7, because HOME is checked on windows and sometimes set to Document folder (which is wrong)
    if os.name == \'nt\':
        if \'USERPROFILE\' in os.environ:
            path = os.environ[\'USERPROFILE\']
        else:
            try:
                drive = os.environ[\'HOMEDRIVE\']
            except KeyError:
                drive = \'\'
            path = os.path.join(drive, os.environ[\'HOMEPATH\'])
    path = os.path.join(path, ".assetninja", *parts)
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return path


def environment_path(*parts):
    return runtime_path(environment_name(), *parts)


def registry_root_path(*parts):
    return environment_path(\'registry\', *parts)
''', sys.modules["gaffer_assetexchange.assetexchange_shared.common.environment"].__dict__)

exec('''from .environment import *
''', sys.modules["gaffer_assetexchange.assetexchange_shared.common"].__dict__)

exec('''import itertools


def explode_variants(assemblyName, variants):
    if assemblyName not in variants:
        return ([], [])
    # build cartesian product out of provided variants
    labels = list(variants[assemblyName].keys())
    configs = itertools.product(*list(variants[assemblyName].values()))
    return (labels, configs)


def filter_objects_by_variant_config(asset, assemblyName, variantLabels, variantConfig):
    if assemblyName not in asset[\'assemblies\']:
        return []

    def filter_by_config(obj):
        for obj_variant in obj[\'variants\']:
            matches = True
            for idx, label in enumerate(variantLabels):
                if variantConfig[idx] != obj_variant[label]:
                    matches = False
            if matches:
                return True
        return False
    return list(filter(filter_by_config, list(asset[\'assemblies\'][assemblyName][\'objects\'].values())))
''', sys.modules["gaffer_assetexchange.assetexchange_shared.asset.variants"].__dict__)

exec('''from .variants import *
''', sys.modules["gaffer_assetexchange.assetexchange_shared.asset"].__dict__)

exec('''
class AssetPushServiceInterface:
    # lists all supported asset types which can be pushed here
    def SupportedTypes(self, _):
        return []

    # checks if specific asset can be pushed here
    def PushAllowed(self, asset):
        return False

    # reacts to asset push intent
    def Push(self, data):
        return False
''', sys.modules["gaffer_assetexchange.assetexchange_shared.server.services"].__dict__)

exec('''import os
from .. import common


def registration_path(category, type):
    return os.path.join(common.registry_root_path(category, type), str(os.getpid()))
''', sys.modules["gaffer_assetexchange.assetexchange_shared.server.registry"].__dict__)

exec('''import json
import logging

try:
    from BaseHTTPServer import BaseHTTPRequestHandler
except ImportError:
    from http.server import BaseHTTPRequestHandler
try:
  basestring
except NameError:
  basestring = str

class HttpServerRequestHandler(BaseHTTPRequestHandler):
    # retrieves logger (will be overriden)
    def get_logger(self):
        return logging.getLogger()

    # retrieves service registry (will be overriden)
    def get_service_registry(self):
        return {}

    # apply our logging mechanism
    def log_message(self, format, *args):
        #logger = self.get_logger()
        #logger.info(format % args)
        pass

    # handle post request
    def do_POST(self):
        logger = self.get_logger()
        try:
            # load and parse request
            req_raw = self.rfile.read(int(self.headers.get(\'content-length\')))
            req_msg = {
                "id": 0,
                "address": None,
                "input": None,
                "final": True
            }
            req_msg.update(json.loads(req_raw))
            try:
                # validate request
                if \'address\' not in req_msg or not isinstance(req_msg[\'address\'], basestring):
                    raise RuntimeError(\'address_missing\')
                if \'final\' not in req_msg or req_msg[\'final\'] != True:
                    raise RuntimeError(\'request_not_final\')
                # extract service and function name
                address_parts = req_msg[\'address\'].split(".")
                service_name = ".".join(address_parts[:-1])
                function_name = address_parts[-1]
                # lookup service
                service_registry = self.get_service_registry()
                if service_name not in service_registry or service_registry[service_name] is None:
                    raise RuntimeError(\'unknown_service\')
                service_class = service_registry[service_name]
                service = service_class()
                # lookup function
                function = getattr(service, function_name, None)
                if not callable(function):
                    raise RuntimeError(\'unknown_function\')
                # call function (will be delegated to main thread automatically, when annotated)
                logger.info(\'executing \' + req_msg[\'address\'])
                res_msg = {
                    "id": req_msg["id"],
                    "output": function(req_msg["input"]),
                    "error": None,
                    "last": True
                }
                # write response
                self.send_response(200)
                self.send_header(\'Content-type\', \'application/json\')
                self.end_headers()
                self.wfile.write(json.dumps(res_msg).encode())
            except Exception as e:
                logger.exception("exception occured in post handler")
                # prepare response
                res_msg = {
                    "id": req_msg["id"],
                    "output": None,
                    "error": str(e),
                    "last": True
                }
                # write response
                self.send_response(200)
                self.send_header(\'Content-type\', \'application/json\')
                self.end_headers()
                self.wfile.write(json.dumps(res_msg).encode())
        except Exception as e:
            logger.exception("exception occured in post handler")
            # write response
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.end_headers()

    def end_headers(self):
        self.send_header(\'Access-Control-Allow-Origin\', \'*\')
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header(\'Access-Control-Allow-Methods\', \'GET, POST, OPTIONS\')
        BaseHTTPRequestHandler.end_headers(self)
''', sys.modules["gaffer_assetexchange.assetexchange_shared.server.protocol"].__dict__)

exec('''from .protocol import *
from .registry import *
from .services import *
''', sys.modules["gaffer_assetexchange.assetexchange_shared.server"].__dict__)

exec('''import os
import json
from .. import common

def lookup_port(category, type):
    regDir = common.registry_root_path(category, type)
    pidfiles = [fn for fn in os.listdir(regDir) if (
        os.path.isfile(os.path.join(regDir, fn)) and fn.isdigit())]
    if len(pidfiles) > 0:
        with open(os.path.join(regDir, pidfiles[0]), \'r\') as file:
            node = json.loads(file.read())
            return node[\'port\']
    else:
        raise RuntimeError(\'could not lookup port for \' +
                           category + \'/\' + type)
''', sys.modules["gaffer_assetexchange.assetexchange_shared.client.registry"].__dict__)

exec('''import json

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

def call_basic_func(port, service, function, input, timeout):

    # prepare url
    url = "http://127.0.0.1:" + str(port) + "/.rpc/basic"

    # prepare timeout
    if timeout == 0:
        timeout = 10

    # prepare request message
    reqMsg = {
        \'id\': 0,
        \'address\': service + \'.\' + function,
        \'input\': input,
        \'final\': True
    }
    reqMsgByte = json.dumps(reqMsg).encode(\'utf8\')

    # execute request
    req = Request(
        url, data=reqMsgByte, method="POST",
        headers={\'content-type\': \'application/json\'}
    )

    # read response message
    res = urlopen(req, timeout=timeout)
    resMsg = json.loads(res.read().decode(\'utf-8\'))

    # raise error if one occured
    if resMsg[\'error\'] is not None:
        raise RuntimeError(resMsg[\'error\'])

    return resMsg[\'output\']
''', sys.modules["gaffer_assetexchange.assetexchange_shared.client.basic"].__dict__)

exec('''from .basic import *
from .registry import *
''', sys.modules["gaffer_assetexchange.assetexchange_shared.client"].__dict__)

exec('''from . import common
from . import asset
from . import client
from . import server
''', sys.modules["gaffer_assetexchange.assetexchange_shared"].__dict__)

exec('''import queue
import threading

_main_thread_exec_queue = queue.Queue()


def main_thread_handler():
    had_work = not _main_thread_exec_queue.empty()
    while not _main_thread_exec_queue.empty():
        task = _main_thread_exec_queue.get()
        try:
            task[\'return\'] = task[\'function\'](*task[\'args\'], **task[\'kwargs\'])
        except Exception as e:
            task[\'exception\'] = str(e)
        task[\'completion\'].set()
    if had_work:
        return 0.1
    return 0.2


def execute_on_main_thread(original_function):
    def new_function(*args, **kwargs):
        # skip delegation, if we are on main thread alread
        if threading.current_thread() is threading.main_thread():
            return original_function(*args, **kwargs)
        completion_event = threading.Event()
        queue_item = {
            \'function\': original_function,
            \'args\': args,
            \'kwargs\': kwargs,
            \'return\': None,
            \'exception\': None,
            \'completion\': completion_event
        }
        _main_thread_exec_queue.put(queue_item)
        # wait for result
        completion_event.wait()
        # raise exception if required
        if queue_item[\'exception\'] is not None:
            raise RuntimeError(queue_item[\'exception\'])
        # return result
        return queue_item[\'return\']
    return new_function
''', sys.modules["gaffer_assetexchange.assetexchange_blender.mainthread"].__dict__)

exec('''import os
import time
import threading
import http
import json
import sys
import atexit
import logging
import bpy
import gaffer_assetexchange.assetexchange_shared as assetexchange_shared
from . import mainthread


_http_servers = dict()


def register_addon(addon_uid, addon_info, AssetPushService=None, misc_services={}):
    # prevent double registration
    global _http_servers
    if addon_uid in _http_servers:
        raise RuntimeError(\'add-on already registered\')

    # prepare logger
    logger = logging.getLogger(addon_uid)
    logger.setLevel(logging.INFO)

    # add console handler
    if not hasattr(logger, \'_has_console_handler\'):
        console_log = logging.StreamHandler()
        console_log.setLevel(logging.DEBUG)
        console_log.setFormatter(logging.Formatter(
            \'%(asctime)s - %(name)s - %(levelname)s - %(message)s\'))
        logger.addHandler(console_log)
        setattr(logger, \'_has_console_handler\', True)

    # check if push service is derived properly
    if AssetPushService is not None:
        if not issubclass(AssetPushService, assetexchange_shared.server.AssetPushServiceInterface):
            raise RuntimeError(
                \'AssetPushService should inherit AssetPushServiceInterface\')

    # setup registry
    service_registry = {}
    if AssetPushService is not None:
        service_registry[\'assetninja.assetpush#1\'] = AssetPushService
    service_registry.update(misc_services)
    service_registry = {key: val for key,
                        val in service_registry.items() if val is not None}

    # setup http protocol handler
    class HttpServerRequestHandler(assetexchange_shared.server.HttpServerRequestHandler):
        # copy logger over
        _logger = logger

        # override logger getter
        def get_logger(self):
            return self._logger

        # copy service registry over
        _service_registry = service_registry

        # override service registry getter
        def get_service_registry(self):
            return self._service_registry

    # start http server using a free port
    _http_servers[addon_uid] = http.server.ThreadingHTTPServer(
        (\'127.0.0.1\', 0),
        HttpServerRequestHandler
    )
    thread = threading.Thread(
        target=_http_servers[addon_uid].serve_forever)
    # note: required for blender exit, otherwhise it will block (even though we have an atexit handler)
    thread.setDaemon(True)
    thread.start()

    # retrieve port (no race condition here, as it is available right after construction)
    port = _http_servers[addon_uid].server_address[1]
    logger.info("port=" + str(port))

    # write registration file
    regfile = assetexchange_shared.server.registration_path(
        \'extension.blender\', addon_uid)
    with open(regfile, \'w\') as portfile:
        portfile.write(json.dumps({
            \'environment\': assetexchange_shared.common.environment_name(),
            \'category\': \'extension.blender\',
            \'type\': addon_uid,
            \'pid\': os.getpid(),
            \'port\': port,
            \'protocols\': [\'basic\'],
            \'info\': {
                \'extension.uid\': addon_uid,
                \'extension.name\': addon_info.get(\'name\', None),
                \'extension.description\': addon_info.get(\'description\', None),
                \'extension.author\': addon_info.get(\'author\', None),
                \'extension.version\': \'.\'.join(map(str, addon_info.get(\'version\'))) if \'version\' in addon_info else None,
                \'blender.executable\': sys.executable,
                \'blender.version\': \'.\'.join(map(str, bpy.app.version)),
                \'blender.user_scripts\': bpy.utils.user_resource(\'SCRIPTS\'),
            },
            \'services\': list(service_registry.keys()),
        }, indent=2))

    # register main thread task handler
    bpy.app.timers.register(mainthread.main_thread_handler,
                            first_interval=1.0, persistent=True)


def unregister_addon(addon_uid):
    # fetch logger
    logger = logging.getLogger(addon_uid)

    # remove main thread task handler
    if bpy.app.timers.is_registered(mainthread.main_thread_handler):
        logger.info(\'removing main thread task handler\')
        bpy.app.timers.unregister(mainthread.main_thread_handler)

    # try to remove registration file
    regfile = assetexchange_shared.server.registration_path(
        \'extension.blender\', addon_uid)
    for _ in range(5):
        if os.path.exists(regfile):
            try:
                logger.info(\'trying to remove registration file\')
                os.remove(regfile)
            except Exception:
                logger.exception(
                    "assetninja: could not remove registration file")
                time.sleep(1)
                continue
            else:
                break
        else:
            break

    # shutdown server
    global _http_servers
    if addon_uid in _http_servers:
        logger.info(\'shutdown http server\')
        _http_servers[addon_uid].shutdown()
        del _http_servers[addon_uid]

    # execute all pending tasks (in my mind this might prevent deadlocks, maybe?)
    mainthread.main_thread_handler()


@atexit.register
def unregister_addons():
    global _http_servers
    for addon_uid in list(_http_servers.keys()):
        unregister_addon(addon_uid)
''', sys.modules["gaffer_assetexchange.assetexchange_blender.addon"].__dict__)

exec('''from .addon import *
from .mainthread import *
''', sys.modules["gaffer_assetexchange.assetexchange_blender"].__dict__)

