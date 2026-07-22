from app.database.mongodb import mongodb


async def create_company(company):

    database = mongodb.db

    existing = await database.companies.find_one(
        {
            "email": company.email
        }
    )

    if existing:
        return {
            "success": False,
            "message": "Company already exists."
        }

    await database.companies.insert_one(
        company.model_dump()
    )

    return {
        "success": True,
        "message": "Company Created Successfully."
    }


async def get_all_companies():

    database = mongodb.db

    companies = await database.companies.find().to_list(100)

    # Convert MongoDB ObjectId to string
    for company in companies:
        company["_id"] = str(company["_id"])

    return companies