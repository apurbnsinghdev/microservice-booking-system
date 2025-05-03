from app.database import get_session, engine
from app.models import Category, SubCategory, Service
from sqlmodel import SQLModel, Session


def seed():
    with Session(engine) as session:
        SQLModel.metadata.create_all(engine)

        #session.exec("DELETE FROM service")
        #session.exec("DELETE FROM subcategory")
        #session.exec("DELETE FROM category")

        #Category
        cat1 = Category(name="AC Repair")
        cat2 = Category(name="Cleaning")

        session.add(cat1)
        session.add(cat2)
        session.commit()

        #SubCategories
        sub1= SubCategory(name="AC Doctor", category_id=cat1.id)
        sub2= SubCategory(name="AC Servicing", category_id=cat1.id)
        sub3= SubCategory(name="Home Cleaning", category_id=cat2.id)
        sub4 = SubCategory(name="Outdoor Cleaning", category_id=cat2.id)

        session.add(sub1)
        session.add(sub2)
        session.add(sub3)
        session.add(sub4)
        session.commit()

        #Services
        srv1 = Service(name="Ac Cooling Problem", description="Trusted & Reliable AC Technicians at home", price=1000, subcategory_id=sub1.id)
        srv2 = Service(name="AC Installation & Uninstallation", description="Trusted & Reliable AC Technicians at service", price=2000, subcategory_id=sub2.id)
        srv3 = Service(name="Full Home Cleaning", description="Cleaning for bathroom, kitchen at home", price=3000, subcategory_id=sub3.id)
        srv4= Service(name="Outdoor Home Cleaning", description="Cleaning for Staircase , Garage at outdoor", price=4000, subcategory_id=sub4.id)
        srv5= Service(name="Outdoor Office Cleaning", description="Cleaning for Office , rooftop at outdoor", price=5000, subcategory_id=sub4.id)
        
        session.add(srv1)
        session.add(srv2)
        session.add(srv3)
        session.add(srv4)
        session.add(srv5)
        session.commit()

if __name__ == "__main__":
    seed()
