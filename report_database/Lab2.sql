SELECT component.id, component_name, component_version_name, license_display 
FROM component
INNER JOIN component_license ON component.id = component_license.component_table_id 
WHERE license_display LIKE '%GNU%'