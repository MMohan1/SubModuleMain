HACONFIG_SECTION = "haconfigs"
HACONFIG_DEBUG = "debug"
HACONFIG_TESTING = 'testing'
HACONFIG_PRODUCTION = 'production'
HACONFIG_ROLLBAR = 'rollbar'
HACONFIG_NEWRELIC = 'newrelic'
HACONFIG_NEW_SCORING = 'new_scoring'
HACONFIG_SESSION_LIFETIME = "session_lifetime"
HACONFIG_SECRET = "secret_key"
HACONFIG_EXCLUDING_COMPANY = "excluding_company"
HACONFIG_VALID_DOMAINS = "valid_domains"
HACONFIG_COMPANY_LOGO = "company_logo"
HACONFIG_KEEN_ENABLE = "keen_enable"
HACONFIG_BLACKLIST = "blacklist"
HACONFIG_HIDE_DEATILS = "hide_details"
HACONFIG_JOBMAIL = "jobmail"
HACONFIG_PREFER_LOCATION = "prefer_location"
HACONFIG_CANDIDATE_FREEZE = "candidate_freeze"
HACONFIG_AGGRIGATION_SIZE = "aggrigation_size"

DEFAULT_HACONFIG_DEBUG = 1
DEFAULT_HACONFIG_TESTING = 0
DEFAULT_HACONFIG_PRODUCTION = 0
DEFAULT_HACONFIG_ROLLBAR = 0
DEFAULT_HACONFIG_NEWRELIC = 0
DEFAULT_HACONFIG_SESSION_LIFETIME = 3
DEFAULT_HACONFIG_EXCLUDING_COMPANY = ""
DEFAULT_HACONFIG_VALID_DOMAINS = ['edgenetworks.in']
DEFAULT_HACONFIG_NEW_SCORING = 0
DEFAULT_HACONFIG_KEEN_ENABLE = 0
DEFAULT_HACONFIG_COMPANY_LOGO = 'http://upload.wikimedia.org/wikipedia/commons/d/d6/Enterprise_buildings_icons.png'
DEFAULT_HACONFIG_BLACKLIST = 0
DEFAULT_HACONFIG_HIDE_DEATILS = 1
DEFAULT_HACONFIG_JOBMAIL = 0
DEFAULT_HACONFIG_PREFER_LOCATION = 1
DEFAULT_HACONFIG_CANDIDATE_FREEZE = 1

# Celery
CELERY_SECTION = "celery"
CELERY_BROKER = 'broker'
CELERY_HOST = 'host'
CELERY_PORT = 'port'
CELERY_VHOST = 'vhost'
CELERY_TIMEZONE = 'timezone'
CELERY_ENABLE_UTC = 'enable_utc'
CELERY_USERNAME = 'username'
CELERY_PASSWORD = 'password'
DEFAULT_CELERY_BROKER = 'amqp'
DEFAULT_CELERY_HOST = 'localhost'
DEFAULT_CELERY_PORT = 5672
DEFAULT_CELERY_VHOST = 'hirealchemy'
DEFAULT_CELERY_TIMEZONE = 'Asia/Kolkata'
DEFAULT_CELERY_ENABLE_UTC = 1
DEFAULT_CELERY_USERNAME = 'hirealchemy'
DEFAULT_CELERY_PASSWORD = 'hirealchemy'

# Elastic search
ELASTIC_SECTION = "elasticconfig"
ELASTIC_HOST = 'elastichosts'
ELASTIC_QUERY_TIMEOUT = 'query_timeout'
ELASTIC_PORT = 'elasticport'
ELASTIC_QUERY_RADIUS = 'query_radius'
DEFAULT_ELASTIC_HOST = ['139.162.4.158']
DEFAULT_ELASTIC_PORT = 9200
DEFAULT_ELASTIC_QUERY_RADIUS = 150
DEFAULT_ELASTIC_QUERY_TIMEOUT = 60000

# Elastic Indexes
ELASTIC_INDEX_SECTION = "elasticindexes"
ELASTIC_INDIASTORE_INDEX = "indiastore_index"
ELASTIC_INDIASTORE_LOG_INDEX = "indiastore_log_index"
ELASTIC_INDIASTORE_DOCTYPE = "indiastore_doctype"
ELASTIC_PARSEDRESUME_INDEX = "parsedresume_index"
ELASTIC_PARSEDRESUME_DOCTYPE = "parsedresume_doctype"
ELASTIC_BOOKS_INDEX = "books_index"
ELASTIC_BOOKS_DOCTYPE = "books_doctype"
ELASTIC_USSTORE_INDEX = "usstore_index"
ELASTIC_USSTORE_DOCTYPE = "usstore_doctype"
DEFAULT_ELASTIC_INDIASTORE_INDEX = "indiastore_prod_test"
DEFAULT_ELASTIC_INDIASTORE_DOCTYPE = "resume"
DEFAULT_ELASTIC_PARSEDRESUME_INDEX = "paresed_resume_information"
DEFAULT_ELASTIC_PARSEDRESUME_DOCTYPE = "resume"
DEFAULT_ELASTIC_BOOKS_INDEX = "books"
DEFAULT_ELASTIC_BOOKS_DOCTYPE = "book"
DEFAULT_ELASTIC_USSTORE_INDEX = 'usstore'
DEFAULT_ELASTIC_USSTORE_DOCTYPE = 'usresumestore'
ELASTIC_HAGEOLOC_INDEX = "hageoloc_index"
DEFAULT_ELASTIC_HAGEOLOC_INDEX = "hageoloc"
ELASTIC_HAGEOLOC_DOCTYPE = "hageoloc_doctype"
DEFAULT_ELASTIC_HAGEOLOC_DOCTYPE = "loc"
ELASTIC_NSDC_INDEX = "nsdc_index"
ELASTIC_NSDC_DOCTYPE = "nsdc_doctype"
DEFAULT_ELASTIC_NSDC_INDEX = "jobseekers"
DEFAULT_ELASTIC_NSDC_DOCTYPE = "resume"
ELASTIC_CRUNCHBASE_INDEX = "crunchbase_index"
ELASTIC_CRUNCHBASE_DOCTYPE = "crunchbase_doctype"
DEFAULT_ELASTIC_CRUNCHBASE_INDEX = "crunchbase"
DEFAULT_ELASTIC_CRUNCHBASE_DOCTYPE = "company"
ELASTIC_NEWCORM_INDEX = "newcorm_skills_index"
ELASTIC_NEWCORM_DOCTYPE = "skills_doctype"
DEFAULT_ELASTIC_NEWCORM_INDEX = "newcorm_skills"
DEFAULT_ELASTIC_NEWCORM_DOCTYPE = "skills"
ELASTIC_SYNONYMS_INDEX = "hirealchemy_skill_index"
ELASTIC_SYNONYMS_DOCTYPE = "hirealchemy_skill_doctype"


# mongo
MONGO_SECTION = 'mongodb'
MONGO_HOST = 'mongohost'
MONGO_PORT = 'mongoport'
MONGODB = 'dbname'
DEFAULT_MONGO_HOST = 'localhost'
DEFAULT_MONGO_PORT = 27017
DEFAULT_MONGODB = 'rudra_hire_config'
# MONGO_CONN_URI = 'mongodb://localhost:27017/'
# SOCIAL_ACTIVITY_INDEX = "social_activity"
# SOCIAL_ACTIVITY_DOC_TYPE = "activity_data"
# ALCHEM


# #Flask secret key
FLASK_SECRET_SECTION = 'flasksecret'
FLASK_SECRET = "secret"


# Resume storage
RESUME_STORAGE_SECTION = 'resume'
RESUME_STORAGE_PATH = "storage_path"
DEFAULT_RESUME_STORAGE_PATH = '~/resumedirectory'
RESUME_EXCLUDE_DOMAIN = 'exclude_domain'
DEFAULT_RESUME_EXCLUDE_DOMAIN = "NothingToExclude"


# Valid domains
VALID_DOMAINS_SECTION = "validdomains"
VALID_DOMAINS = "domains"


# SERVICE URLS
SERVICEURLS_SECTION = "serviceurls"
NEO4J_SERVICE_URL = "neo4j_service_url"
SCORE_SKILL_URL = "score_skill_url"
JD_SERVICE_URL = "jd_service_url"
CRUNCHBASE_ORG_URL = "crunchbase_org_url"
BLACKLIST_SEARCH_URL = "blacklist_search_url"
TIKA_SERVICE_URL = "tika_service_url"
TIKA_META_URL = 'tika_meta_url'
RESUME_PARSE_URL = "resume_parse_url"
RESUME_DESC_PARSE_URL = "resume_desc_parse_url"
RESUME_DETAILS_URL = 'resume_details_url'
INFERRED_SKILL_URL = 'inferred_skill'
DEFAULT_NEO4J_SERVICE_URL = "http://qa.hirealchemy.com:6999/db/data/"
DEFAULT_SCORE_SKILL_URL = "http://qa.hirealchemy.com:1123/processskills"
DEFAULT_JD_SERVICE_URL = "http://qa.hirealchemy.com:1122/process"
DEFAULT_CRUNCHBASE_ORG_URL = "http://api.crunchbase.com/v/2/organizations"
DEFAULT_BLACKLIST_SEARCH_URL = "http://qa.hirealchemy.com:6667/blacklist"
DEFAULT_TIKA_SERVICE_URL = "http://edgeone:9998/tika"
DEFAULT_TIKA_META_URL = "http://edgeone:9998/meta"
DEFAULT_RESUME_DESC_PARSE_URL = "http://qa.hirealchemy.com:4224/parsefile"
DEFAULT_RESUME_DETAILS_URL = "http://qa.hirealchemy.com:4224/parsefile/spacific/details"
DEFAULT_INFERRED_SKILL_URL = 'http://qa.hirealchemy.com:1122/getinferredskill'
DEFAULT_RESUME_PARSE_URL = "http://128.199.165.115:4224/parse"
# shine
SHINE_SECTION = "shine"
SHINE_QUERY_URL = "query_url"
SHINE_RESUME_URL = 'resume_url'
SHINE_COUNT_URL = 'count_url'
SHINE_SEARCH_URL = 'search_url'
SHINE_DOWNLOAD_URL = 'download_url'
SHINE_CANDIDATE_URL = 'candidate_url'
SHINE_MAX_PAGES = 'max_pages'
SHINE_START_PAGE = "start_page"
SHINE_BREAK_POINT = 'break_point'
DEFAULT_SHINE_QUERY_URL = 'http://recruiter.shine.com/api/search/advanced'
DEFAULT_SHINE_RESUME_URL = 'http://recruiter.shine.com/api/v2/candidate/resume/download/'
DEFAULT_SHINE_CANDIDATE_URL = 'http://recruiter.shine.com/api/v2/candidate/'
DEFAULT_SHINE_MAX_PAGES = 1
DEFAULT_SHINE_BREAK_POINT = 3
DEFAULT_SHINE_START_PAGE = 1

# monster
MONSTER_SECTION = "monster"
MONSTER_COUNT_URL = 'count_url'
MONSTER_SEARCH_URL = 'search_url'
MONSTER_DOWNLOAD_URL = 'download_url'
MONSTER_QUERY_URL = "query_url"
MONSTER_START_PAGE = "start_page"
MONSTER_RESUME_URL = 'resume_url'
MONSTER_MAX_PAGES = 'max_pages'
MONSTER_BREAK_POINT = 'break_point'
DEFAULT_MONSTER_QUERY_URL = 'http://monster.hirealchemy.com/query.ashx'
DEFAULT_MONSTER_RESUME_URL = 'https://recruiter.monsterindia.com/v2/resumedatabase/searchresult.html'
MONSTER_EXCLUDE_COMPANY = "monsterindia_exclude_company"
DEFAULT_MONSTER_MAX_PAGES = 1
DEFAULT_MONSTER_BREAK_POINT = 3
DEFAULT_MONSTER_EXCLUDE_COMPANY = []
DEFAULT_MONSTER_START_PAGE = 1


# Times Job
TIMESJOBS_SECTION = "timesjobs"
TIMESJOBS_BASE_DOMAIN = 'base_domain'
TIMESJOBS_QUERY_URL = "query_url"
TIMESJOBS_COUNT_URL = 'count_url'
TIMESJOBS_SEARCH_URL = 'search_url'
TIMESJOBS_DOWNLOAD_URL = 'download_url'
TIMESJOBS_RESUME_URL = 'resume_url'
TIMESJOBS_MAX_PAGES = 'max_pages'
TIMESJOBS_BREAK_POINT = 'break_point'
TIMESJOBS_START_PAGE = "start_page"
DEFAULT_TIMESJOBS_BASE_DOMAIN = 'http://hire.timesjobs.com/'
DEFAULT_TIMESJOBS_QUERY_URL = 'http://hire.timesjobs.com/employer/authenticate.html?tokenId= '
DEFAULT_TIMESJOBS_RESUME_URL = 'http://hire.timesjobs.com/employer/downloadResumeApi.html?'
DEFAULT_TIMESJOBS_MAX_PAGES = 1
DEFAULT_TIMESJOBS_BREAK_POINT = 3
DEFAULT_TIMESJOBS_START_PAGE = 1

# Carrier Builder
CARRIERBUILDER_SECTION = "careerbuilder"
CAREER_BUILDER_HOST = 'host'
DEFAULT_CAREER_BUILDER_HOST = 'http://ws.careerbuilder.com'
CARRIERBUILDER_COUNT_URL = 'count_url'
CARRIERBUILDER_SEARCH_URL = 'search_url'
CARRIERBUILDER_DOWNLOAD_URL = 'download_url'
CARRIERBUILDER_MAX_PAGES = 'max_pages'
CARRIERBUILDER_BREAK_POINT = 'break_point'
CARRIERBUILDER_START_PAGE = "start_page"
DEFAULT_CARRIERBUILDER_MAX_PAGES = 1
DEFAULT_CARRIERBUILDER_BREAK_POINT = 3
DEFAULT_CARRIERBUILDER_START_PAGE = 1

# Monster USA
MONSTERUSA_SECTION = "monsterusa"
MONSTERUSA_COUNT_URL = 'count_url'
MONSTERUSA_SEARCH_URL = 'search_url'
MONSTERUSA_DOWNLOAD_URL = 'download_url'
MONSTERUSA_MAX_PAGES = 'max_pages'
MONSTERUSA_BREAK_POINT = 'break_point'
MONSTERUSA_START_PAGE = "start_page"
DEFAULT_MONSTERUSA_MAX_PAGES = 1
DEFAULT_MONSTERUSA_BREAK_POINT = 3
DEFAULT_MONSTERUSA_START_PAGE = 1

# INDEED
INDEED_SECTION = "indeed"
INDEED_COUNT_URL = 'count_url'
INDEED_SEARCH_URL = 'search_url'
INDEED_DOWNLOAD_URL = 'download_url'
INDEED_API_TOKEN = 'api_token'
INDEED_MAX_PAGES = 'max_pages'
INDEED_BREAK_POINT = 'break_point'
INDEED_START_PAGE = "start_page"
DEFAULT_INDEED_MAX_PAGES = 1
DEFAULT_INDEED_BREAK_POINT = 3
DEFAULT_INDEED_START_PAGE = 1


# LOGGING
LOGGING_SECTION = 'logging'
LOGGING_FILENAME = 'filename'
LOGGING_INSTANCE = 'instance_name'
DEFAULT_LOGGING_FILENAME = "hirealchemy_flask.log"
DEFAULT_LOGGING_INSTANCE = 'development'

REDIS_SECTION = 'redis'
REDIS_HOST = 'host'
REDIS_PORT = 'port'
AUTOSOURCE_RESUMEIDS_EXPIRE = 'autosource_resumeidslist_expiry'
DEFAULT_REDIS_HOST = 'localhost'
DEFAULT_REDIS_PORT = 6379


# APOSTLE
APOSTLE_SECTION = 'apostle'
APOSTLE_ACTIVATE_URL = 'activate_url'
APOSTLE_KEY = 'apostle_key'
APOSTLE_RESET_TEMPLATE = 'reset_mail_template'
APOSTLE_PASSWORD_URL = 'reset_password_url'
APOSTLE_TEMPLATE_SLUG = 'template_slug'

# ROLLBAR
ROLLBAR_SECTION = 'rollbar'
ROLLBAR_SERVER = 'server'
ROLLBAR_CLIENT = 'client'
ROLLBAR_ENVIRON = 'environ'

# KEEN
KEEN_SECTION = 'keen'
KEEN_PROJECT = 'projectid'
KEEN_WRITE_KEY = 'writekey'
KEEN_READ_KEY = 'readkey'

# INTERCOM
INTERCOM_SECTION = 'intercom'
INTERCOM_APPID = 'appid'
INTERCOM_KEY = 'key'

# ILP
ILP_SECTION = 'ilp'
ILP_GB_KEY = "gbkey"

# alchemy
ALCHEMY_SECTION = 'alchemy'
ALCHEMY_KEY = "key"

# NSDC
NSDC_SECTION = 'nsdc'
NSDC_START_DATE = 'start_date'
NSDC_END_DATE = 'end_date'
NSDC_GRP = "grp"
NSDC_USER_ID = "user_id"
NSDC_COMAPNY_ID = "company_id"
DEFAULT_NSDC_START_DATE = "2015-07-01 08:38:42"
DEFAULT_NSDC_END_DATE = "2015-07-31 08:38:42"
DEFAULT_NSDC_GRP = "NSDC_CANDIDANT"
DEFAULT_NSDC_USER_ID = "485e079f-32ca-4623-b2d7-d3a4be55fed5"
DEFAULT_NSDC_COMAPNY_ID = "e261a028-50c0-4a38-8ecb-29e00471106e"

# pocreport
POCREPORT_SECTION = 'pocreport'
POCREPORT_COMPANYID = 'company_id'
POCREPORT_PROJECTID = 'project_id'
POCREPORT_POSITIONID = 'position_id'
POCREPORT_CLIENT = "client_name"

# jobmail
JOBMAIL_SECTION = 'jobmail'
JOBMAIL_TEMPLATE = 'template'
JOBMAIL_SUBACCOUNT = 'subaccount'
JOBMAIL_APPID = 'app_id'
JOBMAIL_SENDER = 'sender'
JOBMAIL_REPLYTO = "reply_to"
JOBMAIL_CLICKURL = 'click_url'
JOBMAIL_SUBJECT = 'subject'
JOBMAIL_MAIL_LIMIT = 'mail_limit'
JOBMAIL_IMAGE_URL = 'company_image'
MASTER_KEY = "master_key"
###############################
REPORT_POSITIONS = {}



#resumeupdate
RESUMEUPDATE_SECTION = "resumeupdate"
RESUMEUPDATE_MODIFIED_RULE = "modified_rule"
RESUMEUPDATE_DOWNLOAD_DAYS = "download_days"
DEFAULT_RESUMEUPDATE_MODIFIED_RULE = 0
DEFAULT_RESUMEUPDATE_DOWNLOAD_DAYS = 50 


###############ROLE/USER MANAGEMENT#######################
##########PERMISSIONS#############
USER_ACTIVATION = "user_activation"
MODIFY_USER_ROLE = "modify_user_role"
MODIFY_COMPANY_PROFILE = "modify_company_profile"
MODIFY_AUTO_SOURCE_PROVIDERS = "modify_auto_source_providers"
VIEW_USERS = "view_users"
DELETE_ROLE = "delete_role"
CREATE_ROLE = "create_role"
VIEW_ROLES = "view_roles"
MODIFY_ROLE_ACTIONS = "modify_role_actions"
VIEW_ALL_PROJECTS = "view_all_projects"
VIEW_ALL_POSITIONS = "view_all_positions"
CREATE_PUBLIC_PROJECT = "create_public_project"
CREATE_PRIVATE_PROJECT = "create_private_project"
EDIT_PROJECT = "edit_project"
HOLD_RESUME_PROJECT = "hold_resume_project"
ARCHIVE_PROJECT = "archive_project"
ADD_REMOVE_MEMBERS_PROJECT = "add_remove_members_project"
CHANGE_PUBLIC_PRIVATE_PROJECT = "change_public_private_project"
CREATE_PUBLIC_POSITION = "create_public_position"
CREATE_PRIVATE_POSITION = "create_private_position"
VIEW_PUBLIC_PROJECTS = "view_public_projects"
EDIT_POSITION = "edit_position"
HOLD_RESUME_POSITION = "hold_resume_position"
ARCHIVE_POSITION = "archive_position"
ADD_REMOVE_MEMBERS_POSITION = "add_remove_members_position"
MODIFY_POSITION_SOURCE_SETTINGS = "modify_position_source_settings"
AUTOSOURCE_PUBLIC_POSITION = "autosource_public_position"
AUTOSOURCE_PRIVATE_POSITION = "autosource_private_position"
CHANGE_PUBLIC_PRIVATE_POSITION = "change_public_private_position"
OPEN_CLOSE_POSITION = "open_close_position"
VIEW_PUBLIC_POSITION = "view_public_position"
MOVE_FORWARD_CANDIDATE = "move_forward_candidate"
MOVE_BACKWARD_CANDIDATE = "move_backward_candidate"
CREATE_PROJECT = 'create_project'
CREATE_CANDIDATE = 'create_candidate'
VIEW_REPORTS = 'view_reports'

#######DEFAULT ROLES##########
#IMPORTANT SHOULD NOT CHANGE
ADMIN = 'ADMIN'
PROJECT_MANAGER ='PROJECT MANAGER'
TEAM_LEAD = 'TEAM LEAD'
RECRUITER = 'RECRUITER'
DEFAULT_ROLE = 'DEFAULT ROLE'
API_ACCESS = 'API ACCESS'

#######ACTION CATEGORIES#####
ADMIN_ACTIONS = 'admin_actions'
DOMAIN_ACTIONS = 'domain_actions'
PROJECT_ACTIONS = 'project_actions'
POSITION_ACTIONS = 'position_actions'
CANDIDATE_ACTIONS = 'candidate_actions'

#########DEFAULT TYPES########
#IMPORTANT SHOULD NOT CHANGE
ADMIN_TYPE = 'ADMIN TYPE'
USER_TYPE = 'USER TYPE'
VIEW_TYPE = 'VIEW TYPE'
##########PROJECT ACTIONS#######
ARCHIVE='archive'
HOLD='hold'
UNHOLD='unhold'
CREATE_POSITION='create_position'
VIEW='view'
##########ADD MEMBER#############
ADD_MEMBER = 'add_member'
REMOVE_MEMBER = 'remove_member'

##########POSITION ACTIONS#######
# CLOSE = 'close'
CLOSE_REOPEN = 'close_reopen'
# REOPEN = 'reopen'
MODIFY_SOURCE_SETTINGS = "modify_source_settings"
EDIT_SKILLS = "edit_skills"
SOURCE_CANDIDATES = "source_candidates"
MODIFY_CANDIDATE_STATUSES = "modify_candidate_statuses"
CREATE_TEMPLATE = "create_template"
EXCLUDE_CANDIDATE = "exclude_candidate"

#################
ACTION_NAME = 'action_name'
DISPLAY_NAME = 'display_name'
STATUS = 'status'
#################
MESSAGE='message'
SUCCESS='success'
##########ROLE CATEGORY########
DOMAINTYPE='domaintype'
PROJECTTYPE='projecttype'
POSITIONTYPE='positiontype'

#################
S3_SECTION = 's3'
s3_access_key = "access_key"
s3_secret_key = "secret_key"
s3_bucket_name = "bucket_name"
s3_public_bucket_name= "public_bucket_name"
s3_public_access_key = "public_access_key"
s3_public_secret_key = "public_secret_key"

#################
AUTOSOURCING_SECTION="autosourcing"
AUTOSOURCING_SEARCHTYPE="searchtype"
AUTOSOURCING_NEED_PREFERRED_LOC="need_preferred_loc"
AUTOSOURCING_REQUESTER_NOTIFY_URL="requester_notify_url"
AUTOSOURCING_SOURCE_REGISTRATION_URL="source_registration_url"
AUTOSOURCING_REQUESTER_NOTIFY_URL_DOWNLOAD="requester_notify_url_download"
AUTOSOURCING_THRESHOLD_COUNT = "threshold_count"
AUTOSOURCING_NOTIFICATION_URL_DOWNLOAD = "notification_url_download"
AUTOSOURCING_BUCKET_NAME = "bucket_name"
INDEED_VALID_COUNTRIES = "indeed_valid_countries"

##################
GEOCODE_SECTION="geocode"
GEOCODE_GEO_CODE_URL="geo_code_url" 

############ROLE LOGGING########
CREATED = 'created'
MODIFIED = 'modified'
DELETED = 'deleted'
APPROVED = 'approved'
USER_ACTIVATED = 'user_activated'
USER_DEACTIVATED = 'user_deactivated'
ROLE_CHANGED = 'role_changed'
ROLE_ASSIGNED = 'role_assigned'
ADDED_PROJECTMEMBER = 'added_projectmember'
REMOVED_PROJECTMEMBER = 'removed_projectmember'
ADDED_POSITIONMEMBER = 'added_positionmember'
REMOVED_POSITIONMEMBER = 'removed_positionmember'
###ROLE LOGGING COLLECTION NAMES######
ROLE = "Role"
USER = "User"
PROJECTMEMBERSHIP = "ProjectMembership"
POSITIONMEMBERSHIP = "PositionMembership"
####API USER NAME#####
API_USER = "APIuser"

##################
INDEED_SECTION="indeed"
INDEED_JOB_POST_URL="job_post_url"
INDEED_APPLY_CANDIDATE_URL = "indeed_apply_candidate_url"
#elastic query
FILTER = "elastic_filter"
RANGE_FILTER_NAME = "range_filter"
RANGE_FILTERS = ["salary","experience"]
TERM_FILTER_NAME = "term_filter"
TERM_FILTER = ["locations","site_tag","pref_job_loc","current_employer","degree_institute"]
COMPARISON_FILTER_NAME = "comparison_filter"
COMPARISON_FILTER = ["days"]
SEARCH_FILTER_NAME = "search_filter"
SEARCH_FILTER = ["keyword"]

#HA FILTER
HA_FILTER = "ha_elastic_filter"
HA_RANGE_FILTER_NAME = "range_filter"
HA_RANGE_FILTERS = ["salary","experience"]
HA_TERM_FILTER_NAME = "term_filter"
HA_TERM_FILTER = ["location","source_name","prefer_location","company","organization"]
HA_SEARCH_FILTER_NAME = "search_filter"
HA_COMPARISON_FILTER = ["days"]
HA_COMPARISON_FILTER_NAME = "comparison_filter"
HA_SEARCH_FILTER = ["keyword"]

#SCORE FACTOR
HA_FACTOR = "ha_factor"
FUNCTION_FACTOR_NAME="function"
FUNCTION_FACTOR_SCORE=0.2
PRIMARY_FACTOR_NAME="primary"
PRIMARY_FACTOR_SCORE=2
INFERRED_FACTOR_NAME="inferred"
INFERRED_FACTOR_SCORE=3

#Version
VERSION = "version"

#Platforms
TALEO ="taleo"
PLATFORM = "platform"

FILE_VALID_EXTENSIONS = '(".doc", ".docx", ".html", ".htm", ".odt", ".pdf", ".xls", ".xlsx", ".ods",  ".ppt", ".pptx", ".txt" )'



FIREBASE_SECTION = "firebase"
FIREBASE_TYPE = "type"
FIREBASE_PROJECT_ID = "project_id"
FIREBASE_PRIVATE_KEY_ID = "private_key_id"
# FIREBASE_PRIVATE_KEY = "private_key"
FIREBASE_CLIENT_EMAIL = "client_email"
FIREBASE_CLIENT_ID = "client_id"
FIREBASE_AUTH_URI = "auth_uri"
FIREBASE_TOKEN_URI = "token_uri"
FIREBASE_AUTH_PROVIDER_x509_CERT_URL = "auth_provider_x509_cert_url"
FIREBASE_CLIENT_x509_CERT_URL = "client_x509_cert_url"
FIREBASE_DATABSE_URL = "database_url"



