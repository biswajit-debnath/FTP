**Show State data**
----
  Returns json data about a state corona cases.

* **URL**

  /api/getData/:state

* **Method:**

  `GET`
  
*  **URL Params**

   **Example:**
 
   `/api/getData/assam`


* **Success Response:** <br />

    **Content:** `{"status":200,"state":"assam","current_data":{"confirmed":90,"recovered":41,"deaths":45,"total":176}}`
 
* **Error Response:**<br />
  If you entered a state that is not in dataset<br />
    **Content:** `{"status":200 , error : "No such state found" }`


**Post State data**
----
  Post json data about a state corona cases.

* **URL**

  /api/postData

* **Method:**

  `POST`
  
*  **Body**

   **Example:**
 
   `{ state:"assam", confirmed: 86, recovered: 41, deaths:2 }`


* **Success Response:** <br />

    **Content:** `{ "status":200 }`
 
* **Error Response:**<br />
  If there is no data in the post body<br />
    **Content:** `{status:400,error:"No data posted"}` <br />
  If cache-error occured  <br />
    **Content:** `{status:400,error:"Some error occured try again"}` <br />
  If there is DB error<br />
    **Content:** `{status:400,error:DB error response}`



