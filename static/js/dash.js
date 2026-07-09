// ======================================
// Sidebar Navigation
// ======================================

function showSection(id, btn) {

    document.querySelectorAll(".page").forEach(page => {
        page.classList.remove("active");
    });

    document.getElementById(id).classList.add("active");

    document.querySelectorAll(".menu").forEach(menu => {
        menu.classList.remove("active");
    });

    btn.classList.add("active");
}

console.log("Dashboard JS Loaded");


// ======================================
// CATEGORY UPDATE
// ======================================

document.querySelectorAll(".update-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("updateCategoryName").value =
            this.dataset.name;

        document.getElementById("updateCategoryForm").action =
            "/update_category/" + this.dataset.id + "/";

    });

});


// ======================================
// CATEGORY DELETE
// ======================================

document.querySelectorAll(".delete-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("deleteCategoryForm").action =
            "/delete_category/" + this.dataset.id + "/";

    });

});



// ======================================
// POST UPDATE
// ======================================

document.querySelectorAll(".update-post-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("updatePostTitle").value =
            this.dataset.title;

        document.getElementById("updatePostForm").action =
            "/update_post/" + this.dataset.id + "/";

    });

});



// ======================================
// POST DELETE
// ======================================

document.querySelectorAll(".delete-post-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("deletePostForm").action =
            "/delete_post/" + this.dataset.id + "/";

    });

});



// ======================================
// USER UPDATE
// ======================================

document.querySelectorAll(".update-user-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("updateUserName").value =
            this.dataset.name;

        document.getElementById("updateUserEmail").value =
            this.dataset.email;

        document.getElementById("updateUserForm").action =
            "/update_user/" + this.dataset.id + "/";

    });

});



// ======================================
// USER DELETE
// ======================================

document.querySelectorAll(".delete-user-btn").forEach(button => {

    button.addEventListener("click", function () {

        document.getElementById("deleteUserForm").action =
            "/delete_user/" + this.dataset.id + "/";

    });

});