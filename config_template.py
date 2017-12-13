__author__ = 'rudragouda'

import constants

template_dict = {
    constants.CELERY_SECTION: {constants.CELERY_BROKER: constants.DEFAULT_CELERY_BROKER,
                               constants.CELERY_HOST: constants.DEFAULT_CELERY_HOST,

                               constants.CELERY_PORT: constants.DEFAULT_CELERY_PORT,
                               constants.CELERY_VHOST: constants.DEFAULT_CELERY_VHOST,
                               constants.CELERY_TIMEZONE: constants.DEFAULT_CELERY_TIMEZONE,
                               constants.CELERY_ENABLE_UTC: constants.DEFAULT_CELERY_ENABLE_UTC,
                               constants.CELERY_USERNAME: constants.DEFAULT_CELERY_USERNAME,
                               constants.CELERY_PASSWORD: constants.DEFAULT_CELERY_PASSWORD
                               },

    constants.ELASTIC_SECTION: {constants.ELASTIC_HOST: constants.DEFAULT_ELASTIC_HOST,
                                constants.ELASTIC_PORT: str(constants.DEFAULT_ELASTIC_PORT),
                                constants.ELASTIC_QUERY_RADIUS: str(constants.DEFAULT_ELASTIC_QUERY_RADIUS),
                                constants.ELASTIC_QUERY_TIMEOUT: str(constants.DEFAULT_ELASTIC_QUERY_TIMEOUT)},

    constants.ELASTIC_INDEX_SECTION: {
        constants.ELASTIC_BOOKS_DOCTYPE: constants.DEFAULT_ELASTIC_BOOKS_DOCTYPE,
        constants.ELASTIC_BOOKS_INDEX: constants.DEFAULT_ELASTIC_BOOKS_INDEX,
        constants.ELASTIC_INDIASTORE_DOCTYPE: constants.DEFAULT_ELASTIC_INDIASTORE_DOCTYPE,
        constants.ELASTIC_INDIASTORE_INDEX: constants.DEFAULT_ELASTIC_INDIASTORE_INDEX,
        constants.ELASTIC_PARSEDRESUME_DOCTYPE: constants.DEFAULT_ELASTIC_PARSEDRESUME_DOCTYPE,
        constants.ELASTIC_PARSEDRESUME_INDEX: constants.DEFAULT_ELASTIC_PARSEDRESUME_INDEX,
        constants.ELASTIC_HAGEOLOC_INDEX: constants.DEFAULT_ELASTIC_HAGEOLOC_INDEX,
        constants.ELASTIC_HAGEOLOC_DOCTYPE: constants.DEFAULT_ELASTIC_HAGEOLOC_DOCTYPE,
        constants.ELASTIC_USSTORE_INDEX: constants.DEFAULT_ELASTIC_USSTORE_INDEX,
        constants.ELASTIC_USSTORE_DOCTYPE: constants.DEFAULT_ELASTIC_USSTORE_DOCTYPE,
        constants.ELASTIC_NSDC_DOCTYPE: constants.DEFAULT_ELASTIC_NSDC_DOCTYPE,
        constants.ELASTIC_NSDC_INDEX: constants.DEFAULT_ELASTIC_NSDC_INDEX,
        constants.ELASTIC_CRUNCHBASE_DOCTYPE: constants.DEFAULT_ELASTIC_CRUNCHBASE_DOCTYPE,
        constants.ELASTIC_CRUNCHBASE_INDEX: constants.DEFAULT_ELASTIC_CRUNCHBASE_INDEX,
        constants.ELASTIC_NEWCORM_DOCTYPE: constants.DEFAULT_ELASTIC_NEWCORM_DOCTYPE,
        constants.ELASTIC_NEWCORM_INDEX: constants.DEFAULT_ELASTIC_NEWCORM_INDEX},

    constants.LOGGING_SECTION: {constants.LOGGING_FILENAME: constants.DEFAULT_LOGGING_FILENAME,
                                constants.LOGGING_INSTANCE: constants.DEFAULT_LOGGING_INSTANCE},

    constants.MONGO_SECTION: {constants.MONGODB: constants.DEFAULT_MONGODB,
                              constants.MONGO_HOST: constants.DEFAULT_MONGO_HOST,
                              constants.MONGO_PORT: constants.DEFAULT_MONGO_PORT},

    constants.MONSTER_SECTION: {
        constants.MONSTER_BREAK_POINT: str(constants.DEFAULT_MONSTER_BREAK_POINT),
        constants.MONSTER_MAX_PAGES: str(constants.DEFAULT_MONSTER_MAX_PAGES),
        constants.MONSTER_QUERY_URL: constants.DEFAULT_MONSTER_QUERY_URL,
        constants.MONSTER_START_PAGE: constants.DEFAULT_MONSTER_START_PAGE,
        constants.MONSTER_RESUME_URL: constants.DEFAULT_MONSTER_RESUME_URL,
        constants.MONSTER_EXCLUDE_COMPANY: constants.DEFAULT_MONSTER_EXCLUDE_COMPANY
    },

    constants.CARRIERBUILDER_SECTION: {
        constants.CARRIERBUILDER_BREAK_POINT: str(constants.DEFAULT_CARRIERBUILDER_BREAK_POINT),
        constants.CARRIERBUILDER_MAX_PAGES: str(constants.DEFAULT_CARRIERBUILDER_MAX_PAGES),
        constants.CARRIERBUILDER_START_PAGE: constants.DEFAULT_CARRIERBUILDER_START_PAGE,
    },

    constants.MONSTERUSA_SECTION: {
        constants.MONSTERUSA_BREAK_POINT: str(constants.DEFAULT_MONSTERUSA_BREAK_POINT),
        constants.MONSTERUSA_MAX_PAGES: str(constants.DEFAULT_MONSTERUSA_MAX_PAGES),
        constants.MONSTERUSA_START_PAGE: constants.DEFAULT_MONSTERUSA_START_PAGE,
    },

    constants.INDEED_SECTION: {
        constants.INDEED_BREAK_POINT: str(constants.DEFAULT_INDEED_BREAK_POINT),
        constants.INDEED_MAX_PAGES: str(constants.DEFAULT_INDEED_MAX_PAGES),
        constants.INDEED_START_PAGE: constants.DEFAULT_INDEED_START_PAGE,
    },

    constants.RESUME_STORAGE_SECTION: {
        constants.RESUME_STORAGE_PATH: constants.DEFAULT_RESUME_STORAGE_PATH,
        constants.RESUME_EXCLUDE_DOMAIN: constants.DEFAULT_RESUME_EXCLUDE_DOMAIN},

    constants.SERVICEURLS_SECTION: {constants.BLACKLIST_SEARCH_URL: constants.DEFAULT_BLACKLIST_SEARCH_URL,
                                    constants.CRUNCHBASE_ORG_URL: constants.DEFAULT_CRUNCHBASE_ORG_URL,
                                    constants.JD_SERVICE_URL: constants.DEFAULT_JD_SERVICE_URL,
                                    constants.NEO4J_SERVICE_URL: constants.DEFAULT_NEO4J_SERVICE_URL,
                                    constants.RESUME_DESC_PARSE_URL: constants.DEFAULT_RESUME_DESC_PARSE_URL,
                                    constants.RESUME_PARSE_URL: constants.DEFAULT_RESUME_PARSE_URL,
                                    constants.RESUME_DETAILS_URL: constants.DEFAULT_RESUME_DETAILS_URL,
                                    constants.SCORE_SKILL_URL: constants.DEFAULT_SCORE_SKILL_URL,
                                    constants.TIKA_SERVICE_URL: constants.DEFAULT_TIKA_SERVICE_URL,
                                    
                                    constants.INFERRED_SKILL_URL: constants.DEFAULT_INFERRED_SKILL_URL,
                                    constants.TIKA_META_URL: constants.DEFAULT_TIKA_META_URL},

    constants.SHINE_SECTION: {constants.SHINE_BREAK_POINT: str(constants.DEFAULT_SHINE_BREAK_POINT),
                              constants.SHINE_MAX_PAGES: str(constants.DEFAULT_SHINE_MAX_PAGES),
                              constants.SHINE_QUERY_URL: constants.DEFAULT_SHINE_QUERY_URL,
                              constants.SHINE_RESUME_URL: constants.DEFAULT_SHINE_RESUME_URL,
                              constants.SHINE_START_PAGE: constants.DEFAULT_SHINE_START_PAGE,
                              constants.SHINE_CANDIDATE_URL: constants.DEFAULT_SHINE_CANDIDATE_URL},

    constants.TIMESJOBS_SECTION: {constants.TIMESJOBS_BASE_DOMAIN: constants.DEFAULT_TIMESJOBS_BASE_DOMAIN,
                                 constants.TIMESJOBS_BREAK_POINT: constants.DEFAULT_TIMESJOBS_BREAK_POINT,
                                 constants.TIMESJOBS_MAX_PAGES: constants.DEFAULT_TIMESJOBS_MAX_PAGES,
                                 constants.TIMESJOBS_START_PAGE: constants.DEFAULT_TIMESJOBS_START_PAGE,
                                 constants.TIMESJOBS_QUERY_URL: constants.DEFAULT_TIMESJOBS_QUERY_URL,
                                 constants.TIMESJOBS_RESUME_URL: constants.DEFAULT_TIMESJOBS_RESUME_URL},

    constants.HACONFIG_SECTION: {constants.HACONFIG_DEBUG: constants.DEFAULT_HACONFIG_DEBUG,
                                 constants.HACONFIG_NEWRELIC: constants.DEFAULT_HACONFIG_NEWRELIC,
                                 constants.HACONFIG_PRODUCTION: constants.DEFAULT_HACONFIG_PRODUCTION,
                                 constants.HACONFIG_ROLLBAR: constants.DEFAULT_HACONFIG_ROLLBAR,
                                 constants.HACONFIG_SESSION_LIFETIME: constants.DEFAULT_HACONFIG_SESSION_LIFETIME,
                                 constants.HACONFIG_VALID_DOMAINS: constants.DEFAULT_HACONFIG_VALID_DOMAINS,
                                 constants.HACONFIG_NEW_SCORING: constants.DEFAULT_HACONFIG_NEW_SCORING,
                                 constants.HACONFIG_COMPANY_LOGO: constants.DEFAULT_HACONFIG_COMPANY_LOGO,
                                 constants.HACONFIG_EXCLUDING_COMPANY: constants.DEFAULT_HACONFIG_EXCLUDING_COMPANY,
                                 constants.HACONFIG_KEEN_ENABLE: constants.DEFAULT_HACONFIG_KEEN_ENABLE,
                                 constants.HACONFIG_TESTING: constants.DEFAULT_HACONFIG_TESTING,
                                 constants.HACONFIG_BLACKLIST: constants.DEFAULT_HACONFIG_BLACKLIST,
                                 constants.HACONFIG_HIDE_DEATILS:constants.DEFAULT_HACONFIG_HIDE_DEATILS,
                                 constants.HACONFIG_JOBMAIL:constants.DEFAULT_HACONFIG_JOBMAIL,
                                 constants.HACONFIG_PREFER_LOCATION:constants.DEFAULT_HACONFIG_PREFER_LOCATION},

    constants.REDIS_SECTION: {constants.REDIS_HOST: constants.DEFAULT_REDIS_HOST,
                              constants.REDIS_PORT: constants.DEFAULT_REDIS_PORT},

    constants.NSDC_SECTION: {constants.NSDC_START_DATE: constants.DEFAULT_NSDC_START_DATE,
                             constants.NSDC_END_DATE: constants.DEFAULT_NSDC_END_DATE,
                             constants.NSDC_GRP: constants.DEFAULT_NSDC_GRP,
                             constants.NSDC_USER_ID: constants.DEFAULT_NSDC_USER_ID,
                             constants.NSDC_COMAPNY_ID: constants.DEFAULT_NSDC_COMAPNY_ID},

    constants.RESUMEUPDATE_SECTION: {constants.RESUMEUPDATE_MODIFIED_RULE: constants.DEFAULT_RESUMEUPDATE_MODIFIED_RULE,
                                     constants.RESUMEUPDATE_DOWNLOAD_DAYS: constants.DEFAULT_RESUMEUPDATE_DOWNLOAD_DAYS},
    
    constants.FILTER: {constants.RANGE_FILTER_NAME: constants.RANGE_FILTERS,
                       constants.TERM_FILTER_NAME: constants.TERM_FILTER,
                       constants.SEARCH_FILTER_NAME: constants.SEARCH_FILTER,
                       constants.COMPARISON_FILTER_NAME: constants.COMPARISON_FILTER
                   },
    constants.HA_FILTER: {constants.HA_RANGE_FILTER_NAME: constants.HA_RANGE_FILTERS,
                       constants.HA_TERM_FILTER_NAME: constants.HA_TERM_FILTER,
                       constants.HA_SEARCH_FILTER_NAME: constants.HA_SEARCH_FILTER,
                       constants.HA_COMPARISON_FILTER_NAME: constants.HA_COMPARISON_FILTER
                      },

    constants.HA_FACTOR: {constants.FUNCTION_FACTOR_NAME: constants.FUNCTION_FACTOR_SCORE,
                       constants.PRIMARY_FACTOR_NAME: constants.PRIMARY_FACTOR_SCORE,
                       constants.INFERRED_FACTOR_NAME: constants.INFERRED_FACTOR_SCORE
                      }
}
