from decouple import config
from service import get_service
from account import GTMAccount
from container import GTMContainer
from gtm_controller import GTMController
from workspace import GTMWorkspace
from tag import GTMTag
from trigger import GTMTrigger
#from variable import GTMVariable

CLIENT_SECRETS = config('CLIENT_SECRETS')
ACCOUNT_ID = config('ACCOUNT_ID')
CONTAINER_NAME= config('CONTAINER_NAME')
CONTAINER_ID = config('CONTAINER_ID')
WORKSPACE_NAME = config('WORKSPACE_NAME')
WORKSPACE_ID = config('WORKSPACE_ID')

scope = ['https://www.googleapis.com/auth/tagmanager.edit.containers']
service = get_service('tagmanager', 'v2', scope, CLIENT_SECRETS)


### GTM OVERVIEW ###
gtm_controller = GTMController(service)

# account_list = gtm_controller.get_account_list()
# gtm_controller.print_account_list(account_list)
# container_list = gtm_controller.get_container_list(ACCOUNT_ID)
# gtm_controller.print_container_list(container_list)
# workspace_list = gtm_controller.get_workspace_list(ACCOUNT_ID, CONTAINER_ID)
# gtm_controller.print_workspace_list(workspace_list)
# tag_list = gtm_controller.get_tag_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_tag_list(tag_list)
# trigger_list = gtm_controller.get_trigger_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_trigger_list(trigger_list)
# custom_variable_list = gtm_controller.get_custom_variable_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_custom_variable_list(custom_variable_list)
# built_in_variable_list = gtm_controller.get_built_in_variable_list(ACCOUNT_ID, CONTAINER_ID, WORKSPACE_ID)
# gtm_controller.print_built_in_variable_list(built_in_variable_list)


### GTM ACCOUNT ###
accounts = gtm_controller.accounts
account = GTMAccount(accounts, ACCOUNT_ID)
account_path = account._path()

### GTM CONTAINER ###
containers = gtm_controller.containers
container = GTMContainer(containers, account_path, CONTAINER_NAME)
container_path = container._path()

### GTM WORKSPACE ###
workspaces = gtm_controller.workspaces
workspace = GTMWorkspace(workspaces, container_path, WORKSPACE_NAME)
workspace_path = workspace._path()
#workspace_count = gtm_controller.count_workspace(workspace_list)
#new_workspace = workspace._create(container_path, 'NEW_GTM_WS', workspace_count)


### GTM TAG SETUP ###
### TODO : INPUT UI (Django) + Postgres DB  

script = '<script>....</script>'
html_tag_info = {'tag_name':'HTML_TAG', 'tag_type':'html', 'script':script}
  
ga_pv_tag_info = {'tag_name':'GA_PV_TAG', 'tag_type':'ua', 'ua_id':'UA-1234-5'}
ga_event_tag_info = {'tag_name':'GA_EVENT_TAG', 'tag_type':'ua', 'ua_id':'UA-1234-5', 'ga_settings':'{{Google Analytics settings}}', 'non_interaction':'false', 'event_category':'ec-y', 'event_action':'ea-y', 'event_label':'el-yy'}
  
gads_conv_tag_info = {'tag_name':'GADS_CONV_TAG', 'tag_type':'awct', 'conv_id':'12345', 'conv_label':'label1123'}
gads_rm_tag_info = {'tag_name':'GADS_RM_TAG', 'tag_type':'sp', 'conv_id':'12345', 'conv_label':'label1123'}

flc_tag_info = {'tag_name':'FLOODLIGHT_COUNT_TAG', 'tag_type':'flc', 'advertiser_id':'555', 'group_tag':'666', 'activity_tag':'2222', 'count_method':'STANDARD'}
fls_tag_info = {'tag_name':'FLOODLIGHT_SALES_TAG2', 'tag_type':'fls', 'advertiser_id':'555', 'group_tag':'666', 'activity_tag':'2222', 'count_method':'TRANSACTIONS', 'revenue':'1000', 'order_id':'id-yyyy'}


tag = GTMTag(workspaces)
#html_tag = tag._create_html(workspace_path, html_tag_info)
#ga_pv_tag = tag._create_ga_pageview(workspace_path, ga_pv_tag_info)
#ga_event_tag = tag._create_ga_event(workspace_path, ga_event_tag_info)
#gads_conv_tag = tag._create_gads(workspace_path, gads_conv_tag_info)
#gads_rm_tag = tag._create_gads(workspace_path, gads_rm_tag_info)
#flc_tag = tag._create_flc(workspace_path, flc_tag_info)
#fls_tag = tag._create_fls(workspace_path, fls_tag_info)
#tag._info(fls_tag)

### GTM TRIGGER SETUP ###
pv_trigger_info = {'trigger_name':'PV_TRIGGER', 'trigger_type':'pageview'}
click_trigger_info = {'trigger_name':'CLICK_TRIGGER', 'trigger_type':'click'}

trigger = GTMTrigger(workspaces)
#pv_trigger = trigger._create_trigger(workspace_path, pv_trigger_info)
#click_trigger = trigger._create_trigger(workspace_path, click_trigger_info)
#trigger._info(pv_trigger)


### GTM TAG + TRIGGER CONNECT ###
fls_tag = tag._get_tag_by_name(workspace_path, 'FLOODLIGHT_SALES_TAG2')
pv_trigger = trigger._get_trigger_by_name(workspace_path, 'PV_TRIGGER')
tag._connect_with_trigger(fls_tag, pv_trigger)


### GTM VARIABLE SETUP ###

# variable = workspace.create_variable(...)

## TODO: create version

# version = workspace.create_version("Global Update Workspace")

## TODO: publish
# version.publish()
