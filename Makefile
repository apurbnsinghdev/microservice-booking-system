# Makefile to simplify running microservices 🚀

.PHONY: run-catalog run-cart run-slot

# Run Catalog Service
run-catalog:
	uvicorn services.catalog_service.app.main:app --reload --host 0.0.0.0 --port 8001

# Run Cart Service
run-cart:
	uvicorn services.cart_service.app.main:app --reload --host 0.0.0.0 --port 8002

# Run Slot Service
run-slot:
	uvicorn services.slot_service.app.main:app --reload --host 0.0.0.0 --port 8003
