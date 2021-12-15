var stripe = Stripe(
  "pk_test_51K5kkkSJJe1bpxbmb27t7Qvnm0cZNM1MKuhRFO7H63DNluVC4BXo23isisdyLGIn4uMMy2ldVNgIfdhU24MWB7QZ002h6j7E8H"
);

var elem = document.getElementById("submit");
clientsecret = elem.getAttribute("data-secret");

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
  base: {
    color: "#000",
    lineHeight: "2.4",
    fontSize: "16px",
  },
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

card.on("change", function (event) {
  var displayError = document.getElementById("card-errors");
  if (event.error) {
    displayError.textContent = event.error.message;
    $("#card-errors").addClass("alert alert-info");
  } else {
    displayError.textContent = "";
    $("#card-errors").removeClass("alert alert-info");
  }
});

var form = document.getElementById("payment-form");
form.addEventListener("submit", function (ev) {
  ev.preventDefault();

  var custName = document.getElementById("custName").value;
  var custAdd = document.getElementById("custAdd").value;
  var custAdd2 = document.getElementById("custAdd2").value;
  var postCode = document.getElementById("postCode").value;

  $.ajax({
    type: "POST",
    url: "http://127.0.0.1:8000/orders/add/",
    data: {
      order_key: clientsecret,
      action: "post",
      csrfmiddlewaretoken: CSRF_TOKEN,
    },
    success: function (json) {
      console.log(json);
      stripe
        .confirmCardPayment(clientsecret, {
          payment_method: {
            card: card,
            billing_details: {
              address: {
                line1: custAdd,
                line2: custAdd2,
              },
              name: custName,
            },
          },
        })
        .then(function (result) {
          if (result.error) {
            console.log("payment error");
            console.log(result.error.message);
          } else {
            if (result.paymentIntent.status === "succeeded") {
              console.log("payment processed");
              window.location.replace(
                "http://127.0.0.1:8000/payment/orderplaced/"
              );
            }
          }
        });
    },
    error: function (xhr, errmsg, err) {},
  });
});
