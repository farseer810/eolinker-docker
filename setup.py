#!/usr/bin/python3
#-*- coding: utf-8 -*-
import os
import sys
import traceback

template = """<?php
//主机地址
defined('DB_URL') or define('DB_URL', '{0}');

//主机端口,默认mysql为3306
defined('DB_PORT') or define('DB_PORT', '3306');

//连接数据库的用户名
defined('DB_USER') or define('DB_USER', '{1}');

//连接数据库的密码，推荐使用随机生成的字符串
defined('DB_PASSWORD') or define('DB_PASSWORD', '{2}');

//数据库名
defined('DB_NAME') or define('DB_NAME', '{3}');

//是否允许新用户注册
defined('ALLOW_REGISTER') or define('ALLOW_REGISTER', TRUE);

//是否允许更新项目，如果设置为FALSE，那么自动更新和手动更新都将失效
defined('ALLOW_UPDATE') or define('ALLOW_UPDATE', TRUE);

//网站名称
defined('WEBSITE_NAME') or define('WEBSITE_NAME', '{4}');

//数据表前缀
defined('DB_TABLE_PREFIXION') or define('DB_TABLE_PREFIXION', 'eo');

//语言
defined('LANGUAGE') or define ('LANGUAGE', 'zh-cn');
?>
"""

if __name__ == "__main__":
    try:
        if "IS_REPLICA" in os.environ:
            if "DB_HOST" not in os.environ:
                print("missing DB_HOST setting")
                sys.exit(-1)
            if "DB_NAME" not in os.environ:
                print("missing DB_NAME setting")
                sys.exit(-1)
            if "DB_USER" not in os.environ:
                print("missing DB_USER setting")
                sys.exit(-1)
            if "DB_PASSWORD" not in os.environ:
                print("missing DB_PASSWORD setting")
                sys.exit(-1)

            website_name = os.environ.get('WEBSITE_NAME')
            if "WEBSITE_NAME" not in os.environ:
                website_name = "eoLinker开源版本"
            
            config = template.format(
                os.environ['DB_HOST'],
                os.environ['DB_USER'],
                os.environ['DB_PASSWORD'],
                os.environ['DB_NAME'],
                website_name)
            with open('server/RTP/config/eo_config.php', 'w') as f:
                f.write(config)
    except:
        traceback.print_exc()
        sys.exit(-1) 