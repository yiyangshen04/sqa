import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 1,
  duration: "5s",
  thresholds: {
    checks: ["rate==1.0"],
    http_req_duration: ["p(95)<5000"],
  },
};

export default function () {
  const response = http.get("https://www.sat1.io/");

  check(response, {
    "status is 200": (r) => r.status === 200,
  });

  sleep(1);
}
