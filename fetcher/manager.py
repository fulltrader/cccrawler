'''
Created on 2014.1.8

@author: gaolichuang
'''

from oslo.config import cfg

from miracle.common.utils.gettextutils import _  # noqa
from miracle.common.base import log as logging

from cccrawler.manager import manager
from cccrawler.proto.crawldoc import CrawlDoc

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

class FetcherManager(manager.CrawlManager):
    def __init__(self):
        super(FetcherManager,self).__init__()
    def ProcessCrawlDoc(self,crawldoc):
        LOG.debug(_("ProcessCrawldoc at %(fetch_id)s  crawldoc: %(crawldoc)s"),
                  {'fetch_id':self.m_id,
                   'crawldoc':crawldoc})
