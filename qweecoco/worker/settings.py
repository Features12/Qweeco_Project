# -*- coding: utf-8 -*-
ROLE_DIRECTOR = ROLE_ALL_PRIVILEGES = 'director'  # Роль директора. Имеет все привелегии для модификаций
ROLE_QA = 'qa' # Роль инженера-тестировщика
ROLE_DEVELOPER = 'developer'  # Роль разработчика
ROLE_OFFICE_MANAGER = 'manager'  # Роль офис-менеджера. Имеет все привелегии для модификаций
ROLE_DESIGNER = 'designer'  # Роль дизайнера


# Список дозволенных ролей для модификаций
ROLES_WITH_ALL_PRIVILEGES = [ROLE_DIRECTOR, ROLE_OFFICE_MANAGER]


# Choices для модели Worker
ROLES_EMPLOYEES = (
    (ROLE_DIRECTOR, 'Director'),
    (ROLE_QA, 'Quality assurance'),
    (ROLE_DEVELOPER, 'Developer'),
    (ROLE_OFFICE_MANAGER, 'Office manager'),
    (ROLE_DESIGNER, 'Designer'),
)