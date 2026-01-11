# Software Development Company Management - Odoo Module

A comprehensive Odoo 16 module designed to manage a software development company's operations, including contractor companies, projects, tasks, and subtasks with a robust role-based permission system.

## Features

- **Contractor Companies Management**: Complete CRUD operations for companies that hire your services
- **Project Management**: Extended native Odoo project module with custom fields
- **Task Organization**: Detailed work planning through tasks and subtasks
- **Role-Based Access Control**: Four distinct user roles with granular permissions
- **Full Traceability**: Link each project to its contractor company and tasks to subtasks

## Module Structure

### Custom Models

#### `gestion_software.empresa_contratadora` (Contractor Company)
Custom model to manage companies that contract projects.

**Main Fields:**
- Company name
- Tax ID (CIF)
- Address
- Contact information
- Related contracted projects (One2many relationship)

#### `gestion_software.subtarea` (Subtask)
Custom model to break down tasks into smaller, assignable units of work.

**Main Fields:**
- Name and description
- Related task (Many2one to project.task)
- Assigned user
- Status (Pending, In Progress, Completed, Blocked)
- Priority
- Estimated hours

### Extended Models

#### `project.project` (Inherited)
Extended native Odoo project model with:
- Contractor Company (Many2one relationship)
- Contract date
- Budget

#### `project.task` (Inherited)
Extended native task model with:
- Development Subtasks (One2many relationship)
- Smart button showing subtask count
- Additional methods for subtask management

## User Roles and Permissions

### 1. Administrator
- **Purpose**: System configuration and parameterization
- **Access**: Full access to all entities
- **Note**: Does not participate in daily operations

### 2. Project Manager
- **Purpose**: Overall business management
- **Permissions**:
  - Contractor Companies: Full CRUD
  - Projects: Full CRUD
  - Tasks: Full CRUD
  - Subtasks: Full CRUD
- **Special**: Can modify projects and tasks created by other users

### 3. Analyst
- **Purpose**: Technical planning and task creation
- **Permissions**:
  - Contractor Companies: Read only
  - Projects: Read only
  - Tasks: Full CRUD
  - Subtasks: Full CRUD

### 4. Developer/Programmer
- **Purpose**: Task execution
- **Permissions**:
  - Contractor Companies: Read only
  - Projects: Read only
  - Tasks: Read and Update only (no Create/Delete)
  - Subtasks: Read and Update only (no Create/Delete)

## Workflow

1. **Contractor companies** hire projects
2. **Project Manager** creates the company record and associated project
3. **Project Manager** creates initial tasks and assigns them to **Analysts**
4. **Analysts** break down tasks and assign them to **Developers**
5. **Developers** execute and update task status

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list: `Settings > Apps > Update Apps List`
3. Search for "Gestión de Software"
4. Click Install

## Dependencies

- `base`: Odoo core module
- `project`: Native Odoo project management module
- `mail`: For activity tracking and communication

## Technical Details

### Views Implemented
- **List views (tree)**: For all models
- **Form views**: Detailed forms for all entities
- **Kanban view**: For subtasks with status-based organization
- **Inherited views**: Extended project and task forms

### Security
- **Access Groups**: Four security groups (Administrator, Project Manager, Analyst, Developer)
- **Record Rules**: Domain-based access restrictions
- **Access Rights**: Model-level CRUD permissions defined in `ir.model.access.csv`

### Menu Structure
```
Gestión de Software (Main Menu)
├── Empresas Contratadoras
├── Proyectos
├── Tareas
├── Subtareas
└── Configuración (Admin only)
```

## File Structure

```
gestion_software/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── empresa_contratadora.py
│   ├── subtarea.py
│   ├── project_project.py
│   └── project_task.py
├── views/
│   ├── empresa_contratadora_views.xml
│   ├── subtarea_views.xml
│   ├── project_views.xml
│   └── menus.xml
├── security/
│   ├── security_groups.xml
│   ├── ir.model.access.csv
│   └── record_rules.xml
├── data/
└── static/
    └── description/
```

## Version

- **Module Version**: 16.0.1.0.0
- **Odoo Version**: 16.0
- **License**: LGPL-3

## Contributing

Feel free to submit issues and enhancement requests.

## License

This module is licensed under LGPL-3.

---

**Note**: This module was developed as part of a Business Management Systems course project at IES El Rincón.
