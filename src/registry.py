from .components.menu import render as render_menu
from .components.profile import render as render_profile
from .components.skills import render as render_skills
from .components.projects import render as render_projects
from .components.journey import render as render_journey
from .components.contact import render as render_contact


RENDERERS = {
    "menu": render_menu,
    "profile": render_profile,
    "skills": render_skills,
    "projects": render_projects,
    "journey": render_journey,
    "contact": render_contact,
}