SET @@auto_increment_increment=9;

CREATE TABLE `user_basic` (
    `user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
    `mobile` varchar(11) NOT NULL COMMENT '手机号',
    `password` varchar(93) NOT NULL COMMENT '密码',
    `user_name` varchar(32) NOT NULL COMMENT '用户名',
    `last_login` datetime NULL COMMENT '最后登录时间',
    `email` varchar(20) COMMENT '邮箱',
    `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态，是否可用',
    PRIMARY KEY (`user_id`),
    UNIQUE KEY (`mobile`),
    UNIQUE KEY (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户基本信息表';
