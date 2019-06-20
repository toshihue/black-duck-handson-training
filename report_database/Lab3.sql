SELECT project_name, version_name, count(1)
FROM project_version
INNER JOIN project on project.project_id = project_version.project_id 
INNER JOIN component on project_version.version_id=component.project_version_id 
INNER JOIN component_vulnerability on component_vulnerability.component_table_id = component.id
WHERE (component_vulnerability.severity = 'HIGH' OR component_vulnerability.severity = 'MEDIUM')
AND component_vulnerability.remediation_status = 'NEW'
GROUP BY project_name, version_name