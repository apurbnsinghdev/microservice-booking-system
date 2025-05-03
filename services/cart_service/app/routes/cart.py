import httpx
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_db_session
from app.models.cart import Cart, CartItem, cart_items
from app.models.response import CartResponse, dummy_cart_response
from app.auth import skip_get_current_user


router = APIRouter(prefix="/cart", tags=["Cart"])

SLOT_SERVICE_URL = "http://slot-service:8002"
CATALOG_SERVICE_URL = "http://catalog-service:8001"

def skip_auth_scheme():
    return


@router.post("/{cart_id}/checkout")
def checkout(cart_id: int, current_user=Depends(skip_get_current_user), session: Session = Depends(get_db_session)):
    
    #user_id = current_user["user_id"]

    #cart_items = session.exec(select(CartItem).where(CartItem.user_id == user_id)).all()
    #if not cart_items:
    #    raise HTTPException(status_code=400, detail="Cart is empty")

    # Check Slot availability
    #check_slot(item.partner_id, item.slot_time)

    # Get price from Catalog Service
    total = 0.0
    #for item in session.exec(select(CartItem).where(CartItem.cart_id == cart.id)):
    #price = get_service_price(item.service_id)
    #total += price
    price = 100
    total += price
    #Apply 10% discount
    discount = total * 0.10
    final_total = total - discount


    # Create bookings
    bookings_created = []
    for item in cart_items:
        booking_payload = {
            "user_id": 1,
            "service_id": 1,
            "partner_id": 1,
            "slot_time": datetime.now(),
            "status": "confirmed"
        }
        bookings_created.append(booking_payload)

    #Clear cart
    #for item in cart_items:
    #    session.delete(item)
    #session.commit()

    #Save booking (dummy OMS order_id)
    order_id = f"ORD-1-{int(datetime.utcnow().timestamp())}"

    return {
        "order_id": order_id,
        "total": total,
        "discount": discount,
        "final_total": final_total,
        "booking" : bookings_created
    }

# Call Slot Service 
def check_slot(partner_id: int, slot_time: str):
    with httpx.Client() as client:
        resp = client.get(f"{SLOT_SERVICE_URL}/slots/{partner_id}/{slot_time}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Slot unavailable")
        data = resp.json()
        if not data["available"]:
            raise HTTPException(status_code=400, detail="Slot is fully booked")

#Call Catalog Service
def get_service_price(service_id: int) -> float:
    with httpx.Client() as client:
        resp = client.get(f"{CATALOG_SERVICE_URL}/services/{service_id}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="Service not found")
        data = resp.json()
        return data["price"]

@router.get("/my", response_model=CartResponse, dependencies=[Depends(skip_auth_scheme)])
def get_my_cart(
    session: Session = Depends(get_db_session),
    user: dict = Depends(skip_get_current_user)
):
    
    return dummy_cart_response

@router.post("/add/{service_id}/{partner_id}", dependencies=[Depends(skip_auth_scheme)])
def add_to_cart(
    service_id: int,
    partner_id: int,
    session: Session = Depends(get_db_session),
    user: dict = Depends(skip_get_current_user)
):
    return {"message": "Item added to cart"}

@router.delete("/remove/{item_id}", dependencies=[Depends(skip_auth_scheme)])
def remove_from_cart(
    item_id: int,
    session: Session = Depends(get_db_session),
    user: dict = Depends(skip_get_current_user)
):
    return {"message": "Item removed from cart"}
